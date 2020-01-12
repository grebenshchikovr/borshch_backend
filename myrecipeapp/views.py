from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from authapp.models import BorshchUser
from myrecipeapp.models import MyRecipe
from mainapp.models import Recipe
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def add(request, recipe_pk=None):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    if not MyRecipe.objects.filter(borshchuser=request.user, recipe=recipe).first():

        my_recipe = MyRecipe(borshchuser=request.user, recipe=recipe)
        my_recipe.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, recipe_pk=None):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    my_recipe = MyRecipe.objects.filter(borshchuser=request.user, recipe=recipe).first()

    if my_recipe:
       my_recipe.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

