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
        level = self.request.GET.get('level')
        duration = self.request.GET.get('duration')
        if level:
            list = Recipe.objects.filter(level=level)
        else:
            list = Recipe.objects.all()

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
    level = (
        (None, 'Сложность'),
        ('1', 'Ребенок'),
        ('2', 'Взрослый'),
        ('3', 'Шеф-повар'),
    )

    level = ChoiceField(choices=level, required=False)

class DurationFilterForm(forms.Form):
    FILTER_CHOICES = (
        (None, 'Длительность'),
        (15, '15 минут'),
        (30, '30 минут'),
        (60, '1 час'),
        (61, '> часа'),
    )

    duration = ChoiceField(choices=FILTER_CHOICES, required=False)

