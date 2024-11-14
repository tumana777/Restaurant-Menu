from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from .models import Restaurant, MenuCategory, MenuSubCategory, Dish

from .serializers import (
    RestaurantListSerializer, RestaurantCreateSerializer,
    MenuCategoryListSerializer, MenuCategoryCreateSerializer,
    MenuSubCategoryListSerializer, MenuSubCategoryCreateSerializer,
    DishSerializer, MenuSubCategorySerializer
)

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        restaurant = super().get_object()

        if restaurant.user != self.request.user:
            raise PermissionDenied("You can only update your own restaurant.")

        return restaurant

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.select_related('restaurant')
    serializer_class = MenuCategoryListSerializer

class MenuCategoryCreateView(CreateAPIView):
    serializer_class = MenuCategoryCreateSerializer
    permission_classes = [IsAuthenticated]

class MenuCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = MenuCategory.objects.select_related('restaurant')
    serializer_class = MenuCategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        menu_category = super().get_object()

        if menu_category.restaurant.user != self.request.user:
            raise PermissionDenied("You can only update categories for your own restaurant.")

        return menu_category

class MenuSubCategoryListView(ListAPIView):
    serializer_class = MenuSubCategoryListSerializer

    def get_queryset(self):
        queryset = MenuSubCategory.objects.select_related('menu_category')

        name = self.request.query_params.get('name', None)
        menu_category = self.request.query_params.get('menu_category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if menu_category:
            queryset = queryset.filter(menu_category__name__icontains=menu_category)

        return queryset

class MenuSubCategoryCreateView(CreateAPIView):
    serializer_class = MenuSubCategoryCreateSerializer
    permission_classes = [IsAuthenticated]


class MenuSubCategoryDetailView(RetrieveAPIView):
    serializer_class = MenuSubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MenuSubCategory.objects.select_related('menu_category')

        dish_name = self.request.query_params.get('dish', None)
        subcategory = self.request.query_params.get('subcategory', None)

        if dish_name:
            queryset = queryset.filter(dishes__name__icontains=dish_name)

        if subcategory:
            queryset = queryset.filter(menu_category__name__icontains=subcategory)

        return queryset


class MenuSubCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = MenuSubCategory.objects.select_related('menu_category')
    serializer_class = MenuSubCategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        menu_subcategory = super().get_object()

        if menu_subcategory.menu_category.restaurant.user != self.request.user:
            raise PermissionDenied("You can only update sub categories for your own restaurant.")

        return menu_subcategory

