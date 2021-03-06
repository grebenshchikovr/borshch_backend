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


@register.filter(name='media_folder_cooking_step')
def media_folder_media_folder_cooking_step(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам шагов приготовления
    """
    if not string:
        string = 'cooking_step_photos/default.png'

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
    elif level == 1:
        level = 'child'
    else:
        level = 'none'

    return f'{settings.STATIC_URL}img/level_pic/{level}.png'


@register.filter(name='duration_pic')
def duration_pic(duration):
    """
    заменяет уровень сложности рецепта на его картинку
    """
    if not duration:
        duration ='none'
    elif duration <= 15:
        duration = '15'
    elif duration > 15 and duration <=30:
        duration = '30'
    elif duration > 30 and duration <= 60:
        duration = '60'
    else:
        duration = 'gt_60'


    return f'{settings.STATIC_URL}img/duration_pic/{duration}.png'