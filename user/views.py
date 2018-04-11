from django.shortcuts import render,render_to_response
from .models import Wishlist
from products.models import Products
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from products.models import Products
from django.template.context_processors import csrf
from .models import Profile,Cart
import random
from django.contrib.auth.models import User
@login_required()
def add_to_wishlist(request):
    if request.is_ajax:
        item = request.GET.get('item','')
        #item = Products.objects.get(pk=request.GET.get('item',''))

        if not 'wishlist' in request.session:
            request.session['wishlist'] =[]

        wishlist = request.session['wishlist']
        if item in wishlist:
            wishlist.remove(item)
        else:
            wishlist.append(item)
        request.session['wishlist'] = wishlist
        return JsonResponse({'success':True,'wishlist':wishlist})

@login_required()
def add_to_cart(request):
    if request.is_ajax:
        item = request.GET.get('item','')
        if not 'cart' in request.session:
            request.session['cart'] = []

        cart = request.session['cart']
        if item in cart:
            cart.remove(item)
        else:
            cart.append(item)
        request.session['cart'] = cart
        length=len(request.session['cart'])
        return JsonResponse({'success': True,'length':length, 'cart':cart})

@login_required()
def cart(request):
    c={}
    c.update(csrf(request))
    if 'cart' in request.session:
        cartitems = request.session['cart']
        products = []
        for item in cartitems:
            p = Products.objects.get(pk=int(item))
            products.append(p)
        return render(request,"cart.html",{'products':products})
    else:
        return render(request,"cart.html",c)

@login_required()
def remove_from_cart(request):
    if request.is_ajax:
        item = request.GET.get('item','')
        cart = request.session['cart']
        if item in cart:
            cart.remove(item)
        request.session['cart']=cart
        return JsonResponse({'success':True})

@login_required()
def wishlist(request):
    if 'wishlist' in request.session:
        wishlist = request.session['wishlist']
        products = []
        for item in wishlist:
            p = Products.objects.get(pk=int(item))
            products.append(p)
        return render(request,"wishlist.html",{"products":products})
    else:
        return render(request,"wishlist.html",{})

@login_required()
def remove_from_wishlist(request):
    if request.is_ajax:
        item = request.GET.get('item','')
        wishlist = request.session['wishlist']
        if item in wishlist:
            wishlist.remove(item)
        request.session['wishlist']=wishlist
        return JsonResponse({'success':True})

def profile(request):
    c={}
    c.update(csrf(request))
    profile=Profile.objects.get(user=request.user)
    if profile is not None:
          c.update({"profile":profile})

    return render(request,'profile.html',c)

def updateProfile(request):
    first_name = request.POST.get('firstname','')
    last_name = request.POST.get('lastname','')
    email =request.POST.get('email','')
    phone=request.POST.get('phone','')
    addone=request.POST.get('addone','')
    addtwo=request.POST.get('addtwo','')

    user = request.user
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.save()

    profile=Profile.objects.get(user=request.user)
    if not profile:
        profile=Profile(user=request.user,phone=phone,address_one=addone,address_two=addtwo)
        profile.save()
    else:
        profile.address_one=addone
        profile.address_two=addtwo
        profile.phone=phone
        profile.save()

    return render(request,'profile.html',{"profile":profile,"user":request.user,"success":True})


def my_orders(request):
    cart = Cart.objects.filter(user=request.user)
    orders=[]
    for item in cart:
        order={}
        p=Products.objects.get(pk=item.product.pk)
        order['product']=p.product_name
        order['cart_id']=item.cart_id
        order['quantity']=item.quantity
        order['price']=p.price
        orders.append(order)

    return render(request,'orders.html',{'orders':orders})