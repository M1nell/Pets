from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        return self.category_name

class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name="userBid")


class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    imageURL = models.CharField(max_length=1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name="user")
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null = True, related_name="listingWatchlist")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank = True, null = True, related_name="listingComment")
    message= models.CharField(max_length=300)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"
