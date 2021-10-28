from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

from account.models import Account

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class House(models.Model):
    owner = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="houses")
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    location = models.ForeignKey(City,on_delete=models.RESTRICT)
    type = models.ForeignKey(Category,on_delete=models.RESTRICT)
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    bedrooms = models.IntegerField(validators = [MaxValueValidator(10),MinValueValidator(1)])
    bathrooms = models.IntegerField(validators = [MaxValueValidator(5),MinValueValidator(1)])
    garage = models.BooleanField()
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True)

    class Meta:
        verbose_name_plural = 'Houses'

    def __str__(self):
        return self.name

class HouseImage(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    image = models.TextField(null=True)

    class Meta:
        verbose_name_plural="HouseImages"
    
    def __str__(self):
        return self.image + " | " +str(self.pk)