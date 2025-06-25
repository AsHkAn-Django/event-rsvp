from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart_list/', views.cart_list, name='cart_list'),
]