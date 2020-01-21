from django.db import models
from django.conf import settings


class Unit(models.Model):
    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
    short_name = models.CharField(verbose_name='сокращение', max_length=8, unique=True)
    name = models.CharField(verbose_name='название', max_length=128, blank=True)

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
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
    unit = models.ForeignKey(Unit,  on_delete=models.SET(''))
    name = models.CharField(verbose_name='название ингредиента', max_length=255)

    def __str__(self):
        return f"{self.name} ({self.unit.name})"


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название рецепта', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)
    level = models.IntegerField(verbose_name='сложность приготовления', default=1)
    duration = models.IntegerField(verbose_name='время приготовления', default=15)
    image = models.ImageField(upload_to='recipe_photos', blank=True)

    def __str__(self):
        return f"{self.name} ({self.cuisine.name})"


class Composition(models.Model):
    class Meta:
        verbose_name = 'Пропорция'
        verbose_name_plural = 'Пропорции'
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(verbose_name='количество', max_digits=12, decimal_places=2, default=1)

    def __str__(self):
        return '{} - {}'.format(self.recipe.name, self.ingredient.name)

class CookingStep(models.Model):
    class Meta:
        verbose_name = 'Шаг приготовления'
        verbose_name_plural = 'Шаги приготовления'
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cooking = models.TextField(verbose_name='шаг приготовления', blank=False)
    image = models.ImageField(upload_to='cooking_step_photos', blank=True)

    def __str__(self):
        return self.recipe.name
