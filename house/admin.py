from django.contrib import admin

from house.models import *

admin.site.register(House)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Country)

# Register your models here.
