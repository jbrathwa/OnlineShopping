from django.db import models
from user.models import Cart

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    date = models.DateField()
    payment_mode = models.CharField(max_length=10)
    total_amount = models.FloatField()

    