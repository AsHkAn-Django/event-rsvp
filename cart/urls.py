from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_add/<int:pk>/', views.cart_add, name='cart_add'),
]