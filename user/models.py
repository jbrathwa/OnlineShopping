from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address_one = models.TextField(max_length=500)
    address_two = models.TextField(max_length=500)
    phone=models.CharField(max_length=25)

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_id=models.IntegerField()
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()