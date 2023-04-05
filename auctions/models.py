from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = (
    ("", "Select a Category"),
    ("Books", "Books"),
    ("Music", "Music"),
    ("Beauty", "Beauty"),
    ("Sport", "Sport"),
    ("Electronics", "Electronics"),
    ("Other", "Other")
)


class User(AbstractUser):
    pass


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    start_bid = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=15, choices=CATEGORIES, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.price}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.comment


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='watchlist')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True, related_name='watchlist_items')
    # ...

    objects = models.Manager()

    def __str__(self):
        return f"{self.user} watching {self.listing}"




