from django.shortcuts import render
from products.models import Products
from user.models import Profile
from  django.contrib.auth.models import User
from django.template.context_processors import csrf
# Create your views here.
from user.models import Profile
def checkout(request):
    cartinfo=[]
    cart = request.session['cart']
    for key in cart:
        quantity=request.POST.get('select'+key,'')
        p =Products.objects.get(pk=int(key))
        product={}
        product['product']=p.product_name
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

    return render(request,'checkout.html',{"total":grandtotal,"cart":cartinfo})

def make_order(request):
    c={}
    c.update(csrf(request))
    first_name = request.POST.get('firstname','')
    last_name=request.POST.get('lastname','')
    email=request.POST.get('email','')
    phone=request.POST.get('phone','')
    addone=request.POST.get('addone','')
    addtwo=request.POST.get('addtwo','')

    if request.session['amount']:
        total=request.session['amount']
        c.update({"amount":total})
    return render(request,'payment.html',c)

