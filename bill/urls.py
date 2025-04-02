from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillViewSet

router = DefaultRouter()
router.register(r'bill', BillViewSet, basename='bill')

urlpatterns = [
    path('', include(router.urls)),  # Includes all router-generated URLs
]
