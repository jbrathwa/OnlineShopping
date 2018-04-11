from django.shortcuts import render_to_response,render
from django.contrib.auth.decorators import login_required
from .models import Category,SubCategory,Products,Reviews
from .forms import ProductForm
from django.db.models import Q

@login_required(login_url = "{% url 'login_user' %}")
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

def search(request):
    query=request.GET.get('query')
    print(query)
    products =Products.objects.filter(Q(subcategory__sub_category__istartswith=query)
                                      |Q(category__category__iregex=query)
                                      |Q(subcategory__sub_category__iregex=query)
                                      |Q(subcategory__sub_category__icontains=query)
                                      |Q(product_name__icontains=query)
                                      |Q(product_name__istartswith=query)
                                      |Q(product_name__iregex=query))
    print(products)
    context={"products":products,"search":True}
    return render(request,"display.html",context)


def product(request,product_id):
    product = Products.objects.get(pk=product_id)
    reviews=Reviews.objects.filter(product=product_id)
    if  len(reviews) != 0:
        rating=0
        for r in reviews:
            rating=rating+r.rating
        rating=rating/len(reviews)
    else:
        rating='No Ratings'
    return render(request,'detail.html',{"product":product,"reviews":reviews,"rating":rating})