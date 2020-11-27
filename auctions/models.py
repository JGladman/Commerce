from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=128)

class Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")

class Bids(models.Model):
    amount = models.FloatField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

class Comments(models.Model):
    comment = models.CharField(max_length=128)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
