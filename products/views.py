from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from .models import Category,Product
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer

#GET all categories
@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    categories=Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data)

#CREATE category-only logged in users
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def category_create(request):
    serializer=CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#GET all products-anyone can view
@api_view(['GET'])
@permission_classes([AllowAny])   #anyone can access this API without login
def product_list(request):
    products=Product.objects.filter(is_active=True) #hidden or deleted products won't show
    serializers=ProductSerializer(products,many=True) #serializing list of products
    return Response(serializers.data)

#GET single Product
@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request,pk):  #pk is primary key
    try:
        product=Product.objects.get(id=pk,is_active=True)
    except product.DoesNotExist:  #exception name
        return Response(
            {"error":"Product not found"},status=status.HTTP_404_NOT_FOUND
        )
    serializer=ProductSerializer(product)
    return Response(serializer.data)

#CREATE product-only admin
@api_view(["POST"])
@permission_classes([IsAuthenticated]) #must be logged in first and need JWT token in header
def product_create(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Update Product
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def product_update(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except product.DoesNotExist:
        return Response(
            {"error":"Product Not Found"},status=status.HTTP_404_NOT_FOUND
        )
    serializer=ProductSerializer(product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#DELETE product
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def product_delete(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except product.DoesNotExist:
        return Response(
            {"error":"Product Not Found"},status=status.HTTP_404_NOT_FOUND
        )
    product.is_active=False  #won't actually delete from datbase-soft delete
    product.save()
    return Response({"message":"Product Deleted"},status=status.HTTP_200_OK) 