from django.db import models
from user.models import Cart,Profile

# Create your models here.
class Order(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    cart_id=models.IntegerField()
    date = models.DateField()
    payment_mode = models.CharField(max_length=10)
    total_amount = models.FloatField()

    