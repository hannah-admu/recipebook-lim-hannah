from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    lmodel = Recipe
    inlines = [RecipeIngredientInline,]

class ProfileInLine(admin.StackedInline):
    model = Profile 
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)