from django.shortcuts import render_to_response,render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import generic
from .models import Category,SubCategory,Products
from .forms import ProductForm

#class ProductListView(generic.ListView):
#	    model = Products


#@login_required(login_url = "{% url 'login_user' %}")

def add_product(request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            form=ProductForm()
            context={
                "product":product.product_name,
                "form":form
            }
            product.save()
            return render(request,"addproduct.html",context)
        context = {
            "form": form,
        }
        return render(request, 'addproduct.html',context)

def new_product(request):
    product=request.POST.get('product_name','')
    return render_to_response('addnew.html',{"product":product})

def byCategory(request,category_id):
    category = Category.objects.get(pk=category_id)
    products = Products.objects.filter(category=category_id)
    context={
        "category":category,
        "products":products
    }
    return render(request,"display.html",context)

def bySubCategory(request,category_id,subcategory_id):
    category = Category.objects.get(pk=category_id)
    subcategory = SubCategory.objects.get(pk=subcategory_id)
    products = Products.objects.filter(category=category_id,subcategory=subcategory_id)
    context = {
        "category": category,
        "subcategory": subcategory,
        "products":products
    }
    return render(request, "display.html", context)