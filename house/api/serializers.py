from rest_framework import serializers

from house.models import *
from account.api.serializers import AccountSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        country = CountrySerializer(many=True)
        model = City
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        owner = AccountSerializer(many=True)
        type =  CategorySerializer(many=True)
        location = CitySerializer(many=True)
        model = House
        fields = '__all__'