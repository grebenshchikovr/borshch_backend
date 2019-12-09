from django.shortcuts import render
from .models import Unit, Cuisine, Ingredient, Recipe, Composition
from django.shortcuts import get_object_or_404

def main(request):
    title = 'главная'

    recipes = Recipe.objects.all()
    cuisines = Cuisine.objects.all()

    content = {'title': title, 'recipes': recipes, 'cuisines': cuisines}
    return render(request, 'mainapp/index.html', content)

def recipes(request, pk=None):
    title = 'список рцептов'
    recipes = Recipe.objects.all()
    cuisine = None

    if pk:
            cuisine = get_object_or_404(Cuisine, pk=pk)
            recipes = recipes.filter(cuisine=cuisine)


    content = {'title': title,
               'recipes': recipes,
               'cuisines': Cuisine.objects.all(),
               }
    return render(request, 'mainapp/recipes.html', content)


def recipe(request, pk):
    title = 'просмотр рецепта'
    compositions = Composition.objects.filter(recipe_id=pk)
    content = {
        'title': title,
        'recipe': get_object_or_404(Recipe, pk=pk),
        'compositions': compositions,
    }

    return render(request, 'mainapp/recipe.html', content)

