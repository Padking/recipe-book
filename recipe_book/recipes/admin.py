from django.contrib import admin

from .models import (
    Ingredient,
    Recipe,
)


class IngredientInline(admin.TabularInline):
    model = Ingredient.recipes.through
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]
    exclude = (
        'recipes',
    )
    search_fields = ('title', )
