from django.db import models

class Manufacturer(models.Model): 
    name = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)

class Dealership(models.Model): 
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=11)

class Car(models.Model): 
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    dealership = models.ManyToManyField(Dealership)