from django.shortcuts import render
from rest_framework import generics
from api.serializers import RecipesListSerializer
from mainapp.models import Recipe
# Create your views here.

class RecipesListView(generics.ListAPIView):
    serializer_class = RecipesListSerializer
    queryset = Recipe.objects.all()