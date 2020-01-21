from django.contrib import admin
from .models import Unit, Cuisine, Ingredient, Recipe, Composition, CookingStep

admin.site.register(Unit)
admin.site.register(Cuisine)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Composition)
admin.site.register(CookingStep)