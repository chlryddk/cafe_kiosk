from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_name', 'price', 'category')
    search_fields = ('menu_name', 'category')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','menu','count','customer','date')