from django.shortcuts import render
from .models import Unit, Cuisine, Ingredient, Recipe, Composition
from django.shortcuts import get_object_or_404

def main(request):
    title = 'главная'

    recipes = Recipe.objects.all()
    compositions = Composition.objects.all()
    ingredients = Ingredient.objects.all()

    content = {'title': title, 'recipes': recipes, 'compositions': compositions, 'ingredients': ingredients}
    return render(request, 'mainapp/index.html', content)