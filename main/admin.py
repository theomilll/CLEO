from django.contrib import admin
from .models import FoodProduct, Ingredients, IngredientAdmin


# Register your models here.

admin.site.register(FoodProduct)
admin.site.register(Ingredients, IngredientAdmin)
