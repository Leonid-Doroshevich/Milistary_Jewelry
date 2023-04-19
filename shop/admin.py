from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAmdin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'quantity' , 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price', 'available', 'quantity']
    prepopulated_fields = {'slug': ('name', )}  

