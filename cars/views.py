from rest_framework import viewsets
from cars.models import Car, Brand, Dealer, Listing
from cars.serializers import CarSerializer, BrandSerializer, DealerSerializer, ListingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    # Allow the 'listings' endpoint to filter by Car Brand Name, Car Model, Listing year, Listing Price, Listing Color, Dealer name, Dealer location.
    @action(detail=False)
    def search(self, request):
        listing = False
        if request.GET.get('brand', False):
            listing = Listing.objects.filter(car__brand__name__contains=request.GET.get('brand'))
        if request.GET.get('car', False):
            listing = Listing.objects.filter(car__model__contains=request.GET.get('car'))
        if request.GET.get('year', False):
            listing = Listing.objects.filter(year__contains=request.GET.get('year'))
        if request.GET.get('price', False):
            listing = Listing.objects.filter(price__contains=request.GET.get('price'))
        if request.GET.get('color', False):
            listing = Listing.objects.filter(car__colors__contains=request.GET.get('color'))
        if request.GET.get('dealer', False):
            listing = Listing.objects.filter(dealer__name__contains=request.GET.get('dealer'))
        if request.GET.get('dealer_loc', False):
            listing = Listing.objects.filter(dealer__location__contains=request.GET.get('dealer_loc'))
        if not listing:
            listing = Listing.objects.all()
        serializer = self.get_serializer(listing, many=True)
        return Response(serializer.data)