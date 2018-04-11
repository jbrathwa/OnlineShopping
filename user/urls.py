from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^wishlist$',views.add_to_wishlist,name="add_to_wishlist"),
    url(r'^cart$',views.add_to_cart,name="add_to_cart"),
    url(r'^cartdetail',views.cart,name="cart"),
    url(r'^wishlistinfo',views.wishlist,name="wishlist"),
    url(r'^cart/remove',views.remove_from_cart,name="remove"),
    url(r'^wishlist/remove',views.remove_from_wishlist,name="removelist"),
    url(r'^profile$',views.profile,name="profile"),
    url(r'^updateprofile$',views.updateProfile,name="update_profile"),
    url(r'^orders',views.my_orders,name="my_orders")
]