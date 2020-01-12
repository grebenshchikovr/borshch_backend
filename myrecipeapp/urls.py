from django.urls import path

import myrecipeapp.views as myrecipeapp

app_name = 'myrecipeapp'

urlpatterns = [

    path('remove/<int:recipe_pk>', myrecipeapp.remove, name='remove'),
    path('add/<int:recipe_pk>/', myrecipeapp.add, name='add'),

]