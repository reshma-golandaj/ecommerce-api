#Registeer models in Django admin panal
from django.contrib import admin
from .models import Product,Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','created_at'] #column shows in admin
    search_fields=['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','stock','category','is_active']
    search_fields=['name']  #serach by name
    list_filter=['category','is_active']  #filter by category

