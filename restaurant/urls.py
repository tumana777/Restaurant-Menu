from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantListView, RestaurantCreateView, RestaurantUpdateView,
    MenuCategoryListView, MenuCategoryCreateView, MenuCategoryUpdateView,
    MenuSubCategoryListView, MenuSubCategoryCreateView, MenuSubCategoryUpdateView,
    MenuSubCategoryDetailView
)

app_name = 'restaurants'

router = DefaultRouter()

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('menu-categories/', MenuCategoryListView.as_view(), name='categories'),
    path('menu-categories/create/', MenuCategoryCreateView.as_view(), name='category-create'),
    path('menu-categories/<int:pk>/update/', MenuCategoryUpdateView.as_view(), name='category-update'),
    path('menu-subcategories/', MenuSubCategoryListView.as_view(), name='subcategories'),
    path('menu-subcategories/create/', MenuSubCategoryCreateView.as_view(), name='subcategory-create'),
    path('menu-subcategories/<int:pk>/', MenuSubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('menu-subcategories/<int:pk>/update/', MenuSubCategoryUpdateView.as_view(), name='subcategory-update'),
]