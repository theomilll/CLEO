from django.contrib import admin
from .models import FoodProduct, Ingredients


# Register your models here.

admin.site.register(FoodProduct)
admin.site.register(Ingredients)
