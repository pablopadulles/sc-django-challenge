from django.urls import path, include
from rest_framework import serializers

from cars.models import Car, Brand

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