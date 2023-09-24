from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import User, Listing, Bid, Comment, Watchlist
from django.contrib.auth.decorators import login_required
from datetime import datetime


class CreateForm(forms.Form):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 500)
    image = forms.URLField()

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
    })

def listing(request, id):
    list = Listing.objects.get(id=id)
    comments = list.comments.all()
    return render(request, "auctions/listing.html", {
        "list": list,
        "comments": comments
        
    })
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def bid(request):
    if request.method == "POST":
        bid = float(request.POST['b'])
        id = request.POST['id']
        list = Listing.objects.get(id=id)
        current = list.current_price

        if bid <= current:
           return render(request, "auctions/listing.html", {
               "list": list,
               "message": "Bid too low."
            })
        list.current_price = bid
        list.save()
        return render(request, "auctions/listing.html", {
            "list": list,
            "message": "Bid Applied"
       })

@login_required
def create_listing(request):
    if request.method == "POST":
        title = request.POST['t']
        description = request.POST['d']
        price = request.POST['p']
        image = request.POST['u']
        list = Listing(title=title, description=description, current_price=price, image=image, time=datetime.now())
        list.save()
        return render(request, "auctions/listing.html", {
            "message": "Listing Saved",
            "list": list
        })
    return render(request, "auctions/create.html")


@login_required
def watch_list(request):
    if request.method == "POST":
        id = request.POST['listid']
        list = Listing.objects.get(id=id)
        watch = Watchlist(user=request.user, title=list.title, current_price=list.current_price, description=list.description, image=list.image)
        watch.save()
        watchlist = Watchlist.objects.all()
        return render(request, "auctions/watchlist.html", {
            "id": id,
            "watchlist": watchlist,
            })
    watchlist = Watchlist.objects.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist
    })

@login_required
def comment(request):
    if request.method == "POST":
        text = request.POST['comment']
        id = request.POST['id']
        list = Listing.objects.get(id=id)
        #Listing(title=list.title, description=list.description, current_price=list.price, image=list.image, time=datetime.now())
        return render(request, "auctions/listing.html", {
            "list": list
        })