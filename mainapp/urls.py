from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('recipes/<cuisine>/', mainapp.CuisineRecipeList.as_view(), name='cuisine'),
    path('<int:pk>', mainapp.RecipeDetailView.as_view(), name='recipe'),
    path('', mainapp.RecipeList.as_view(), name='index'),

]
