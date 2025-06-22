from django.urls import path
from . import views

app_name = 'myApp'
urlpatterns = [
    path('join_or_leave/<int:pk>/', views.join_or_leave_event, name='join_or_leave'),
    path('', views.IndexView.as_view(), name='home'),
]
