from django.contrib import admin

from .models import Category, Food

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
