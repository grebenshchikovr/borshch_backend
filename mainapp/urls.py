from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.recipes, name='index'),
    path('cuisine/<int:pk>/', mainapp.recipes, name='cuisine'),
    path('recipe/<int:pk>', mainapp.recipe, name='recipe'),

]
