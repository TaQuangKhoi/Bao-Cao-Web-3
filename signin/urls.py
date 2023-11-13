from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('signin', views.signin, name='signin'),
]