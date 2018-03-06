from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login',views.login_user,name = 'login_user'),
    url(r'^auth/$', views.auth_user,name='auth_user'),
    url(r'^logout/$', views.logout_user,name='logout'),
]