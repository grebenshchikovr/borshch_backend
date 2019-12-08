from django.shortcuts import render
from .models import Unit, Cuisine, Ingredient, Recipe, Composition
from django.shortcuts import get_object_or_404

def main(request):
    title = 'главная'

    recipes = Recipe.objects.all()

    content = {'title': title, 'recipes': recipes,}
    return render(request, 'mainapp/index.html', content)

def recipes(request, pk=None):
    title = 'продукты'

    recipes = Recipe.objects.all()
    if pk != 0:
        cuisine = get_object_or_404(Cuisine, pk=pk)
        recipes = recipes.filter(cuisine__pk=pk).order_by('name')

    content = {'title': title,
               'recipes': recipes,
               'cuisine': Cuisine.objects.all(),

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

