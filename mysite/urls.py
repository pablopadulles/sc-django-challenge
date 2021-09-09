from django.urls import path, include
from rest_framework import routers
from cars.views import CarViewSet, BrandViewSet, DealerViewSet, ListingViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'dealer', DealerViewSet)
router.register(r'listing', ListingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]