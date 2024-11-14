from django.contrib import admin
from .models import Restaurant, MenuSubCategory, MenuCategory, Dish, Ingredient

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuSubCategory)
class MenuSubCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
