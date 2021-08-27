from django.urls import path, include
from rest_framework import routers
from cars.views import CarViewSet, BrandViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]