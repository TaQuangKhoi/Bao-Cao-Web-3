from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('order', views.order, name='order'),
    path('profile', views.profile, name='profile')
]