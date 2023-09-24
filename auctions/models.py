from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null=True, unique = True)

    def __str__(self):
        return f"{self.username}"
class Bid(models.Model):
    new_price = models.DecimalField(max_digits=7, decimal_places=2, default = 0.00)
    
    def __str__(self):
        return f"{self.new_price}"

class Comment(models.Model):

    text = models.CharField(max_length = 1000)

    def __str__(self):
        return f"{self.text}"
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user")
    title = models.CharField(max_length = 200)
    current_price = models.DecimalField(max_digits=7, decimal_places=2, default = 0.00)
    description = models.CharField(max_length = 500)
    image = models.URLField()
    
class Listing(models.Model):
    user = models.ForeignKey(User, default="", on_delete = models.CASCADE, related_name="listinguser")
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    image = models.URLField()
    time = models.DateTimeField()
    comments = models.ManyToManyField(Comment, null = True, related_name="comment")
    current_price = models.DecimalField(max_digits=7, decimal_places=2, default = 0.00)
    category = models.CharField(max_length = 100, default="All")

    def __str__(self):
        return f"{self.title}: {self.id} : {self.current_price} : {self.description} : {self.image}"


admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
admin.site.register(User)