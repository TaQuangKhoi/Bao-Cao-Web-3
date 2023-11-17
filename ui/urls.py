from django.urls import path, include

from caythue import settings
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ranks', views.RanksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('trading/', views.trading, name='trading'),

    path('logout/', views.logout_view, name='Logout'),
]
