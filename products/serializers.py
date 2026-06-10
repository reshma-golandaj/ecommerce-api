from rest_framework import serializers
from .models import Category,Product
class CategorySerializer(serializers.ModelSerializer): #converts category objects to JSON
    class Meta:
        model=Category
        fields=['id','name','description'] #only shows 3 fields in response

class ProductSerializer(serializers.ModelSerializer):
    #show category name instead of just id
    category_name=serializers.CharField(source='category.name',read_only=True) #without this response only shows category_id but with this it also shows category_name
    class Meta:
        model=Product
        fields=['id','name','description','price','stock','image','category','category_name','created_at','is_active']