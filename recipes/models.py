from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание рецепта')
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ингредиента')
    quantity = models.CharField(max_length=100, verbose_name='Количество')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
