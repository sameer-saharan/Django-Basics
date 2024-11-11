from rest_framework import serializers
from .models import *

class ManfSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Manufacturer
        fields = ['name', 'origin']

class DealSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Dealership
        fields = ['name', 'location', 'address', 'contact']

class CarSerializer(serializers.ModelSerializer): 
    dealership = serializers.PrimaryKeyRelatedField(many=True, queryset=Dealership.objects.all())

    class Meta: 
        model = Car
        fields = ['name', 'manufacturer', 'dealership']