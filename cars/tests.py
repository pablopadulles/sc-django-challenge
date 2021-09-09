from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from cars.models import Car, Brand, Dealer, Listing

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

class ListingEndpoint(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.brand = Brand.objects.create(name='Renault')
    self.car = Car.objects.create(model='18', brand=self.brand, colors='BLACK')
    self.dealer = Dealer.objects.create(name='Comercio Demo', location='San Miguel')
    self.listing = Listing.objects.create(car=self.car, price=220, year=2021, dealer=self.dealer)
    self.brand = Brand.objects.create(name='Peugeot')
    self.car = Car.objects.create(model='404', brand=self.brand, colors='RED')
    self.dealer = Dealer.objects.create(name='Comercio Demo', location='San Miguel')
    self.listing = Listing.objects.create(car=self.car, price=100, year=1980, dealer=self.dealer)

  def test_listing(self):
    endpoint = reverse('listing-list')
    response = self.client.get(endpoint)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0].get('price'), 220)

  def test_listing_car_serch(self):
    endpoint = reverse('listing-list')
    response = self.client.get(endpoint + '?car=18')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0].get('price'), 220)

  def test_listing_car_serch(self):
    endpoint = reverse('listing-list')
    response = self.client.get(endpoint + '?car=18')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0].get('price'), 220)

  # TODO no anda! Investigar.
  # def test_listing_color_serch(self):
  #   endpoint = reverse('listing-list')
  #   response = self.client.get(endpoint + '?color=RED')
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)
  #   self.assertEqual(response.data[0].get('price'), 220)
