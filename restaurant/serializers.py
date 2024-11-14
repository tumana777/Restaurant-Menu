from rest_framework import serializers
from .models import Restaurant, MenuCategory, MenuSubCategory, Dish, Ingredient

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')

class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ['user']

class MenuCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ('id', 'name')

class MenuCategoryCreateSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.none(),
        write_only=True
    )

    class Meta:
        model = MenuCategory
        fields = '__all__'
        extra_kwargs = {
            'restaurant': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['restaurant'].queryset = Restaurant.objects.filter(user=user)

class MenuSubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ('name', 'cover_image')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)

class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('name', 'image', 'ingredients')

class MenuSubCategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    class Meta:
        model = MenuSubCategory
        fields = ('name', 'dishes')

class MenuSubCategoryCreateSerializer(serializers.ModelSerializer):
    menu_category = serializers.PrimaryKeyRelatedField(
        queryset=MenuCategory.objects.none(),
        write_only=True
    )

    class Meta:
        model = MenuSubCategory
        fields = '__all__'
        extra_kwargs = {
            'menu_category': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['menu_category'].queryset = MenuCategory.objects.filter(restaurant__user=user)