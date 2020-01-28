from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Unit, Cuisine, Ingredient, Recipe, Composition, CookingStep
from django.shortcuts import get_object_or_404
from django.forms import forms, ChoiceField

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

    def get_queryset(self):
        query = self.request.GET.get('search')
        filter_field = self.request.GET.get('filter_field')
        if filter_field:
            return Recipe.objects.filter(level=filter_field)
        else:
            return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        context['level_form'] = LevelFilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'filter_field': self.request.GET.get('filter_field', ''),
        })
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

class LevelFilterForm(forms.Form):
    FILTER_CHOICES = (
        (None, 'Сложность'),
        ('1', 'Ребенок'),
        ('2', 'Взрослый'),
        ('3', 'Шеф-повар'),
    )
    #search = forms.CharField(default='3')
    filter_field = ChoiceField(choices=FILTER_CHOICES, required=False)

class DurationFilterForm(forms.Form):
    FILTER_CHOICES = (
        (None, 'Длительность'),
        ('15', '15 минут'),
        ('30', '30 минут'),
        ('1', '1 час'),
    )
    #search = models.CharField(default='3')
    filter_field = ChoiceField(choices=FILTER_CHOICES, required=False)