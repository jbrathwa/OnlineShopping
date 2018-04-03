from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect

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
        context = {"user_name": request.user.username, "total_items": 0}
        return render(request,'base.html', context)
    else:
        return render_to_response('login.html', {"error_msg": "Invalid username or password"})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('')