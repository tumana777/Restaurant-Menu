from django.db import models
from django.utils.translation import gettext_lazy as _

class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name=_('User'), related_name='restaurants')
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    phone = models.CharField(max_length=100, verbose_name=_('Phone'))
    cover_image = models.ImageField(upload_to='images/', verbose_name=_('Cover Image'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, verbose_name=_('Restaurant'), related_name='menu_categories')

    def __str__(self):
        return f"{self.restaurant.name} --> {self.name}"

class MenuSubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    menu_category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE, verbose_name=_('Category'), related_name='menu_sub_categories')
    cover_image = models.ImageField(upload_to='images/', verbose_name=_('Cover Image'))

    def __str__(self):
        return f"{self.menu_category} --> {self.name}"

class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Image'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))
    menu_subcategory = models.ForeignKey('MenuSubCategory', on_delete=models.CASCADE, verbose_name=_('Subcategory'), related_name='dishes')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, verbose_name=_('Dish'), related_name='ingredients')

    def __str__(self):
        return self.name