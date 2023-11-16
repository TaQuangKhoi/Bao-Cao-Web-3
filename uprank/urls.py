from django.urls import path
from . import views

urlpatterns = [
    path('', views.up_rank, name='up_rank')
]