from django.db import models


class ColorChoice:
  YELLOW = 'YELLOW'
  RED = 'RED'
  BLACK = 'BLACK'
  WHITE = 'WHITE'
  CHOICES = [
      (YELLOW, YELLOW),
      (RED, RED),
      (BLACK, BLACK),
      (WHITE, WHITE),
    ]


# Create your models here.
class Brand(models.Model):
  name = models.CharField(max_length=20, blank=False, null=False)

  def __str__(self):
    return f'{self.name}'

class Car(models.Model):
  model = models.CharField(max_length=20, blank=False, null=False)
  brand = models.ForeignKey(Brand, null=False, blank=False, on_delete=models.CASCADE)
  colors = models.CharField(max_length=55, choices=ColorChoice.CHOICES, 
  default=ColorChoice.BLACK, null=False, blank=True)

  def __str__(self):
    return f'{self.brand.name} {self.model}'


class Dealer(models.Model):
  name = models.CharField(max_length=20, blank=False, null=False)
  location = models.CharField(max_length=255, blank=False, null=False)

  def __str__(self):
    return f'{self.name}'


class Listing(models.Model):
  car = models.ForeignKey(Car, null=False, blank=False, on_delete=models.CASCADE)
  price = models.FloatField(null=False, blank=False)
  year = models.IntegerField()
  dealer = models.ForeignKey(Dealer, null=False, blank=False, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.dealer.name} {self.car.model}'
