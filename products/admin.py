from django.contrib import admin
from .models import Category,SubCategory,Brand,Products
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products)
admin.site.register(Brand)