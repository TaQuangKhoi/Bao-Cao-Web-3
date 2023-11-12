from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('up_rank/', views.up_rank, name='up_rank'),
    path('trading/', views.trading, name='trading'),
]

