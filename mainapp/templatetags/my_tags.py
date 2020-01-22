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


@register.filter(name='level_pic')
def level_pic(level):
    """
    заменяет уровень сложности рецепта на его картинку
    """

    if level == 2:
        level = 'adult'
    elif level == 3:
        level = 'chief'
    else:
        level = 'child'


    return f'{settings.STATIC_URL}img/level_pic/{level}.png'


@register.filter(name='duration_pic')
def duration_pic(duration):
    """
    заменяет уровень сложности рецепта на его картинку
    """

    if duration <= 15:
        duration = '15'
    elif duration > 15 and duration <=30:
        duration = '30'
    elif duration > 30 and duration <= 60:
        duration = '60'
    else:
        duration = 'gt_60'


    return f'{settings.STATIC_URL}img/duration_pic/{duration}.png'

"""
def collect_url(string):
    return re.sub(<.*>, WORKS, request.resolver_match.route, count=0)
"""