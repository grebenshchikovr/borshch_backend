from django.db import models
from mainapp.models import Recipe
from authapp.models import BorshchUser

class MyRecipe(models.Model):
    class Meta:
        verbose_name = 'Любимый рецепт'
        verbose_name_plural = 'Любимые рецепты'
    borshchuser = models.ForeignKey(BorshchUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.borshchuser.username} ({self.recipe.name})"
