from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.RanksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.dashboard, name='dashboard'),
    path('up_rank/', views.up_rank, name='up_rank'),
    path('trading/', views.trading, name='trading'),
]

