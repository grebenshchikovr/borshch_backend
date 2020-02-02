from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Unit, Cuisine, Ingredient, Recipe, Composition, CookingStep
from django.shortcuts import get_object_or_404
from django import forms

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
        list = super().get_queryset()
        query = self.request.GET.get('search')
        level = self.request.GET.get('level')
        duration = self.request.GET.get('duration')
        ingredient = self.request.GET.get('ingredient')

        # Фильтрация по сложности рецепта
        if level:
            list = Recipe.objects.all().filter(level=level)

        #Фильтрация по длительности приготовления
        if not duration:
            pass
        elif int(duration) <= 15:
            list = list.filter(duration__range=(0, 15))
        elif int(duration) > 15 and int(duration) <= 30:
            list = list.filter(duration__range=(16, 30))
        elif int(duration) > 30 and int(duration) <= 60:
            list = list.filter(duration__range=(31, 60))
        elif int(duration) > 60:
            list = list.filter(duration__gte=60)

        #Исключить рецепты с заданным ингредиентом
        if ingredient:
            for item in list:
                compositions = Composition.objects.all().filter(ingredient__id=ingredient, recipe__id=item.id)
                if compositions:
                    list = list.exclude(name=item.name)

        return list


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        # Add in a QuerySet form to choose level of recipe
        context['level_form'] = LevelFilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'level': self.request.GET.get('level', ''),
        })
        # Add in a QuerySet form to choose duration of recipe
        context['duration_form'] = DurationFilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'duration': self.request.GET.get('duration', ''),
        })
        # Add in a QuerySet form to exclude ingredient
        context['ingredient_form'] = RemoveIngredientFilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'ingredient': self.request.GET.get('ingredient', ''),
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
        list = super().get_queryset()
        self.cuisine = get_object_or_404(Cuisine, name=self.kwargs['cuisine'])
        return list.filter(cuisine=self.cuisine)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        context['cuisine'] = self.cuisine
        return context

class LevelFilterForm(forms.Form):
    level = (
        (None, None),
        (1, 1),
        (2, 2),
        (3, 3),
    )

    level = forms.CharField(label='level', widget=forms.RadioSelect(choices=level, attrs={'id': 'value'}),  required=False, initial='', )

class DurationFilterForm(forms.Form):
    duration = (
        (None, None),
        (15, 15),
        (30, 30),
        (60, 60),
        (61, 61),
    )

    duration = forms.CharField(label='duration', widget=forms.RadioSelect(choices=duration, attrs={'id': 'value'}), required=False, initial=None)

class RemoveIngredientFilterForm(forms.Form):

    ingredient = forms.ModelChoiceField(label='Исключить ингредиент', queryset=Ingredient.objects.all().order_by('name'), required=False)
