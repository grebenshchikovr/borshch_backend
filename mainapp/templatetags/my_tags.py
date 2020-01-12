from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from mainapp.models import Cuisine, Recipe
from myrecipeapp.models import MyRecipe
from authapp.models import BorshchUser

register = template.Library()


@register.filter(name='media_folder_recipes')
def media_folder_recipes(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам рецептов
    """
    if not string:
        string = 'recipe_photos/default.png'

    return f'{settings.MEDIA_URL}{string}'

@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.png'

    return f'{settings.MEDIA_URL}{string}'

@register.filter(name='is_in_fav')
def is_in_fav(recipe_id, user_id):
    """
    Проверяем, есть ли рецепт у юзера в избранном
    """

    myrecipe = MyRecipe.objects.filter(borshchuser=user_id, recipe=recipe_id).first()
    return myrecipe


"""
def collect_url(string):
    return re.sub(<.*>, WORKS, request.resolver_match.route, count=0)
"""