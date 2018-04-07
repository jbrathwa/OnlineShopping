
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^checkout',views.checkout,name="checkout"),
    url(r'^order',views.make_order,name="make_order")
]