from django.urls import path
from Products.views import *


urlpatterns = [
    path('',base,name='base'),

    # Category
    path('category/list/',category_list,name='categorylist'),
    path('category/add/',category_add,name='categoryadd'),
    path('category/edit/<int:id>/',category_edit,name='categoryedit'),
    path('category/delete/<int:id>/',category_delete,name='categorydelete'),


    # Brand
    path('brand/list/',brand_list,name='brandlist'),
    path('brand/add/',brand_add,name='brandadd'),
    path('brand/edit/<int:id>/',brand_edit,name='brandedit'),
    path('brand/delete/<int:id>/',brand_delete,name='branddelete'),



    # Product
    path('product/list/',product_list,name='productlist'),
    path('product/add/',product_add,name='productadd'),
]