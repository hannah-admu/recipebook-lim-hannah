from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

admin.site.register(Ingredient)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecipeIngredientInline]
