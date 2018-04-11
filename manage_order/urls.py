
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^checkout$',views.checkout,name="checkout"),
    url(r'^makeorder',views.make_order,name="make_order"),
    url(r'^payment/(?P<profile_id>\d+)$',views.payment,name="payment"),
    url(r'^order/(?P<paymethod>\w+)(?P<profile_id>\d+)$',views.place_order,name="place_order")
]