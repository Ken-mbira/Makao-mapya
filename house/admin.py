from django.contrib import admin

from house.models import *

admin.site.register(House)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(HouseImage)

# Register your models here.
