from cars.models import Brand, Car, Dealer, Listing
import random

colores = ['YELLOW', 'RED', 'BLACK', 'WHITE']

Brand.objects.create(name='Dacia')
Brand.objects.create(name='Renaut')
Brand.objects.create(name='Peugeot')
Brand.objects.create(name='Chevrolet')
Brand.objects.create(name='Ford')


for idx, brand in enumerate(Brand.objects.all()):
    Car.objects.create(model=str(idx + 1), brand=brand, colors=random.choice(colores))
    Car.objects.create(model=str(idx + 2), brand=brand, colors=random.choice(colores))
    Car.objects.create(model=str(idx + 3), brand=brand, colors=random.choice(colores))

Dealer.objects.create(name='Comercio1', location='San Miguel')
Dealer.objects.create(name='Comercio2', location='CABA')
Dealer.objects.create(name='Comercio3', location='San Isidro')


for dealer in Dealer.objects.all():
    for i in range(5):
        car = random.choice(Car.objects.all())
        precio = float(str(random.randint(19,40)) + '.' + str(random.randint(0,99)))
        year = random.randint(2005, 2021)
        Listing.objects.create(car=car, price=precio, year=year, dealer=dealer)

