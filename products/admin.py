from django.contrib import admin
from .models import Category,SubCategory,Brand,Products,Reviews
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Reviews)