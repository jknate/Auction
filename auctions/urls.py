from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bid", views.bid, name="bid"),
    path("createlisting", views.create_listing, name="createlisting"),
    path("watchlist", views.watch_list, name = "watchlist"),
    path("listing/<str:id>", views.listing, name = "listing"),
    path("listing/<str:id>/comment", views.comment, name = "comment")
]
