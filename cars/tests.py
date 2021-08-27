from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from cars.models import Brand, Car

class TestBrandEndpoint(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.brand = Brand.objects.create(name='Dacia')

  def test_brand_list(self):
    endpoint = reverse('brand-list')
    response = self.client.get(endpoint)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue(response.data[0].get('name') == 'Dacia')

class CarBrandEndpoint(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.brand = Brand.objects.create(name='Renault')
    self.car = Car.objects.create(model='18', brand=self.brand, colors='BLACK')

  def test_car_list(self):
    endpoint = reverse('car-list')
    response = self.client.get(endpoint)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0].get('model'), '18')
    self.assertTrue(response.data[0].get('brand').get('name') == 'Renault')

