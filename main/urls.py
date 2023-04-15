from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.catalog, name='home'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product_detail/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increment_quantity/<int:product_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:product_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('increment_quantity_prod_detail/<int:product_id>/', views.increment_quantity_prod_detail, name='increment_quantity_prod_detail'),
    path('decrement_quantity_prod_detail/<int:product_id>/', views.decrement_quantity_prod_detail, name='decrement_quantity_prod_detail'),
]
