from django.contrib import admin
from .models import FoodProduct, Ingredients, Order


# Register your models here.

admin.site.register(FoodProduct)
admin.site.register(Ingredients)
admin.site.register(Order)
