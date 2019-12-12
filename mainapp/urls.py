from django.urls import path
import mainapp.views as mainapp
from mainapp.views import RecipeList, RecipeDetailView, CuisineRecipeList

app_name = 'mainapp'

urlpatterns = [
    path('recipes/<cuisine>/', CuisineRecipeList.as_view(), name='cuisine'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('', RecipeList.as_view(), name='index'),

]
