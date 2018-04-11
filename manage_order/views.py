from django.shortcuts import render
from products.models import Products
from user.models import Profile
from  django.contrib.auth.models import User
from django.template.context_processors import csrf
import random
from datetime import date
from user.models import Profile,Cart
from .models import Order
def checkout(request):
    cartinfo=[]
    cart = request.session['cart']
    for key in cart:
        quantity=request.POST.get('select'+key,'')
        p =Products.objects.get(pk=int(key))
        product={}
        product['product_id']=p.pk
        product['product']=p.product_name
        product['price']=p.price
        product['quantity']=quantity
        product['total']=p.price*float(quantity)
        cartinfo.append(product)
    if not 'order'in request.session:
        request.session['order']=cartinfo

    grandtotal=0
    for item in cartinfo:
        grandtotal=grandtotal+item['total']

    if not 'amount' in request.session:
        request.session['amount']=grandtotal

    profile=Profile.objects.get(user=request.user)

    return render(request,'checkout.html',{"total":grandtotal,"cart":cartinfo,"profile":profile})

def make_order(request):
    c={}
    c.update(csrf(request))
    phone=request.POST.get('phone','')
    addone=request.POST.get('addone','')
    addtwo=request.POST.get('addtwo','')

    profile = Profile.objects.get(user=request.user)
    if not profile:
        profile = Profile(user=request.user, phone=phone, address_one=addone, address_two=addtwo)
        profile_id=profile.pk
        profile.save()
    else:
        profile.address_one = addone
        profile.address_two = addtwo
        profile.phone = phone
        profile_id=profile.pk
        profile.save()

    if request.session['amount']:
        total=request.session['amount']
        c.update({"amount":total,"profile_id":profile_id})
    return render(request,'payment.html',c)

def payment(request,profile_id):
    c={}
    c.update(csrf(request))
    if request.session['amount']:
        total=request.session['amount']
        c.update({"amount":total,"profile_id":profile_id})

    return render(request,'payment.html',c)

def place_order(request,paymethod,profile_id):
    cart_id=random.randint(1,100000)
    cartinfo=request.session['order']
    cart =request.session['cart']
    for key in cart:
        print(key)
        p = Products.objects.get(pk=int(key))
        for product in cartinfo:
            print(product)
            if product['product_id'] == p.pk:
                c=Cart(user=request.user,product=p,quantity=product['quantity'],cart_id=cart_id)
                c.save()

    del request.session['cart']
    #amount=request.session['amount']
    #order=Order(profile=profile_id,cart_id=cart_id,total_amount=amount,payment_mode=paymethod,date=date.today())

    return render(request,'notification.html',{"order":True})


