from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Unit, Cuisine, Ingredient, Recipe, Composition, CookingStep
from django.shortcuts import get_object_or_404


class MainView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'mainapp/index.html'
    queryset = Recipe.objects.order_by('-id')[:1]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        return context


class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'mainapp/recipes.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        return context


class RecipeDetailView(DetailView):

    model = Recipe
    context_object_name = 'recipe'
    template_name = 'mainapp/recipe.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['composition_list'] = Composition.objects.filter(recipe=self.kwargs['pk'])
        context['cooking_step_list'] = CookingStep.objects.filter(recipe=self.kwargs['pk'])
        context['cuisine_list'] = Cuisine.objects.all()
        return context


class CuisineRecipeList(RecipeList):

    def get_queryset(self):
        self.cuisine = get_object_or_404(Cuisine, name=self.kwargs['cuisine'])
        return Recipe.objects.filter(cuisine=self.cuisine)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        context['cuisine'] = self.cuisine
        return context
