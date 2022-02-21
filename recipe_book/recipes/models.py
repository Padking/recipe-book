from django.db import models


class Recipe(models.Model):
    title = models.CharField('название', max_length=100)
    instruction = models.TextField('порядок приготовления', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredient(models.Model):
    title = models.CharField('название', max_length=100)
    quantity = models.CharField('кол-во с ед. изм.',
                                max_length=25,
                                blank=True)

    recipes = models.ManyToManyField(Recipe,
                                     verbose_name='рецепты',
                                     related_name='ingredients')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
