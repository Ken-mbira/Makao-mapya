from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

from account.models import Account

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Country(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)

class House(models.Model):
    owner = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    location = models.ForeignKey(City,on_delete=models.RESTRICT)
    type = models.ForeignKey(Category,on_delete=models.RESTRICT)
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    bedrooms = models.IntegerField(validators = [MaxValueValidator(10),MinValueValidator(1)])
    bathrooms = models.IntegerField(validators = [MaxValueValidator(5),MinValueValidator(1)])
    garage = models.BooleanField()