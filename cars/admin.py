from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Car, Brand

class CrearAutos(admin.ModelAdmin):
#     brand = Brand.objects.create(name='Renault')
#     car = Car.objects.create(model='18', brand=brand, colors='BLACK')
    pass

#admin.site.register(Brand, AuthorAdmin)
#admin.site.register(Brand, AuthorAdmin)
#admin.site.register(Car, AuthorAdmin)