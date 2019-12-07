from django.db import models
from django.conf import settings


class Unit(models.Model):
    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
    short_name = models.CharField(verbose_name='сокращение', max_length=8, unique=True)
    name = models.CharField(verbose_name='название', max_length=128, unique=True)

    def __str__(self):
        return self.short_name


class Cuisine(models.Model):
    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    unit = models.ForeignKey(Unit,  on_delete=models.SET(''))
    name = models.CharField(verbose_name='название ингредиента', max_length=255)

    def __str__(self):
        return f"{self.name} ({self.unit.name})"


class Recipe(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название рецепта', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f"{self.name} ({self.cuisine.name})"


class Composition(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(verbose_name='количество', max_digits=12, decimal_places=2, default=1)

    def __str__(self):
        return '{} - {}'.format(self.recipe.name, self.ingredient.name)
