from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class Casa(models.Model):
    class CategoryChoices(models.TextChoices):
        APARTAMENTO = "Apartamento"
        CASA = "Casa"
        TERRENO = "Terreno"
    class CityChoices(models.TextChoices):
        SAOJOSE = "São José"
        FLORIPA = "Florianopólis"

    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=15, choices=CityChoices)
    zipcode = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
    photo_main = models.ImageField(upload_to='products/', default='/products/casa.jpg', blank=True)
    photo_1 = models.ImageField(upload_to='products/', default='/products/casa.jpg', blank=True)
    photo_2 = models.ImageField(upload_to='products/', default='/products/casa.jpg', blank=True)

    size = models.DecimalField(max_digits=4, decimal_places=1)
    category = models.CharField(max_length=15, choices=CategoryChoices)
    property_type =models.CharField(max_length=10)
    
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    garage = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title