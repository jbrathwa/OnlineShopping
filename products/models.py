from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)
    is_main =models.BooleanField(default=False)

    def __str__(self):
        return self.category

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category=models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category

class Products(models.Model):
    product_name = models.CharField(max_length=500)
    detail = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Brand(models.Model):
    name=models.CharField(max_length=20,default='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    rating = models.IntegerField()
    review=models.TextField(max_length=500)


