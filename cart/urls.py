from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart-add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart-list/', views.cart_list, name='cart_list'),
]