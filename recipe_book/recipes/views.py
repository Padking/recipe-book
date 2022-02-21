from django.db.models import Q
from django.shortcuts import (
    redirect,
    render,
)
from django.urls import reverse

from .models import (
    Ingredient,
    Recipe,
)


def home(request):
    response = redirect(reverse('recipes'))
    return response


def recipes(request):

    try:
        ingredient_id = int(request.GET.get('ingredient_id'))
    except (ValueError, TypeError):
        ingredient_id = None

    try:
        ingredient_recipe_id = int(request.GET.get('recipe_id'))
    except (ValueError, TypeError):
        ingredient_recipe_id = None

    query = Q()
    if ingredient_id:
        query.add(
            Q(pk=ingredient_id), Q.AND,
        )
    if ingredient_recipe_id:
        query.add(
            Q(recipes__pk=ingredient_recipe_id), Q.AND,
        )

    ingredients_objects = (Ingredient.objects
                           .prefetch_related('recipes').filter(query))

    selected_recipe = Recipe.objects.filter(pk=ingredient_recipe_id)
    selected_ingredient = ingredients_objects.filter(pk=ingredient_id)

    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    ctx = {
        'ingredients': ingredients_objects,
        'selected_recipe': selected_recipe,
        'selected_ingredient': selected_ingredient,
        'form': {
            'description': 'Здесь вы можете ознакомиться с каталогом рецептов',
            'recipe': {
                'title': 'Рецепт',
                'objects': recipes,
                'selected': ingredient_recipe_id,
            },
            'ingredient': {
                'title': 'Ингредиент',
                'objects': ingredients,
                'selected': ingredient_id,
            },
        },
    }

    response = render(request,
                      'recipes/recipes_list.html',
                      ctx)

    return response
