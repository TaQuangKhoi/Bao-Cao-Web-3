from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('logout/', views.logout_view, name='Logout'),
]