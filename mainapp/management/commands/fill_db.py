from django.core.management.base import BaseCommand
from mainapp.models import Cuisine, Unit, Ingredient, Recipe, Composition
from django.contrib.auth.models import User
from authapp.models import BorshchUser

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding="utf8") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):


        cuisines = loadFromJSON('cuisines')

        Cuisine.objects.all().delete()
        for cuisine in cuisines:
            new_cuisine = Cuisine(**cuisine)
            new_cuisine.save()

        units = loadFromJSON('units')

        Unit.objects.all().delete()
        for unit in units:
            new_unit = Unit(**unit)
            new_unit.save()

        ingredients = loadFromJSON('ingredients')

        Ingredient.objects.all().delete()
        for ingredient in ingredients:
            unit_name = ingredient["unit"]
            # Получаем единицу измерения по имени
            _unit = Unit.objects.get(name=unit_name)
            # Заменяем название единицы объектом
            ingredient['unit'] = _unit
            new_ingredient = Ingredient(**ingredient)
            new_ingredient.save()

        recipes = loadFromJSON('recipes')

        Recipe.objects.all().delete()
        for recipe in recipes:
            cuisine_name = recipe["cuisine"]
            # Получаем кухню по имени
            _cuisine = Cuisine.objects.get(name=cuisine_name)
            # Заменяем название кухни объектом
            recipe['cuisine'] = _cuisine
            new_recipe = Recipe(**recipe)
            new_recipe.save()

        compositions = loadFromJSON('compositions')

        Composition.objects.all().delete()
        for composition in compositions:
            recipe_name = composition["recipe"]
            _recipe = Recipe.objects.get(name=recipe_name)
            composition['recipe'] = _recipe
            ingredient_name = composition["ingredient"]
            _ingredient = Ingredient.objects.get(name=ingredient_name)
            composition['ingredient'] = _ingredient

            new_composition = Composition(**composition)
            new_composition.save()

        # Создаем суперпользователя при помощи менеджера модели
        BorshchUser.objects.all().delete()
        BorshchUser.objects.create_superuser('geekbrains', 'geekbrains@geekshop.local', 'geekbrains')
        BorshchUser.objects.create_user('ivan', 'ivan@geekshop.local', 'ivan')
