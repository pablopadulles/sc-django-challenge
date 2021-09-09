from django.urls import path, include
from rest_framework import serializers
from cars.models import Car, Brand, Dealer, Listing

# Serializers define the API representation.
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        depth = 1
        fields = '__all__'


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class DealerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'