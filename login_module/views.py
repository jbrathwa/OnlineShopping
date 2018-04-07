from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from user.models import Profile

def login_user(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_user(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {"error_msg": "Invalid username or password"})


def logout_user(request):
    if 'cart' in request.session:
        del request.session['cart']
    logout(request)
    return HttpResponseRedirect('/')

def newuser(request):
    c={}
    c.update(csrf(request))
    return render_to_response('register.html',c)

def signup(request):
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        rpassword=request.POST.get('rpassword','')
        email=request.POST.get('email','')
        if password == rpassword:
            print(username)
            user=User.objects.create_user(username=username,password=password,email=email)
            profile=Profile(user=user)
            user.save()
            profile.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            return render_to_response("register.html",{'success':False})



