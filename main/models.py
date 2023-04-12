from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Ingredients(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FoodProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='food_products/')
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients, through='ProductsIngredients')

    def __str__(self):
        return self.name


class ProductsIngredients(models.Model):
    productIngredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.Ingredients.name}"


class FoodIngredientInline(admin.TabularInline):
    model = ProductsIngredients
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (FoodIngredientInline,)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
