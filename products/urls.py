from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^add',views.add_product,name="add_product"),
    url(r'^new',views.new_product,name="new_product"),
    url(r'^(?P<category_id>\d+)/(?P<subcategory_id>\d+)$',views.bySubCategory,name="subcategory"),
    url(r'^(?P<category_id>\d+)$',views.byCategory,name="category"),
    #path('products/', views.ProductListView.as_view(), name = 'products'),
]