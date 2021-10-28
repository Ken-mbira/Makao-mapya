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

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        country = CountrySerializer(many=True)
        model = City
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source= 'owner.username')
    class Meta:
        owner = AccountSerializer(many=True,read_only=True)
        model = House
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = '__all__'