from django.shortcuts import render
from products.models import Products,Category
def index(request):
    allproducts ={}
    categories = Category.objects.filter(is_main=True)

    for category in categories:
        products = Products.objects.filter(category=category)[:6]
        if products:
            allproducts[category]=products

    return render(request,"index.html",{"allproducts":allproducts})


