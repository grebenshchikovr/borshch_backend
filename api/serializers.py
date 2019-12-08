from rest_framework import serializers
from mainapp.models import Recipe


class RecipesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'