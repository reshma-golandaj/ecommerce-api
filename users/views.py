from django.shortcuts import render
#view is brain of API ,recieves request from postman and talks to serializer and database then send back response
from rest_framework import status #HTTP status
from rest_framework.decorators import api_view #for using DRF feature
from rest_framework.response import Response #send JSON back to postman
from .serializers import RegisterSerializer #import serializers we created
@api_view(['POST']) #tells Django this function is an API endpoints and accept onlt POST request
def register(request): #request contains all the dataset from postman
    serializer=RegisterSerializer(data=request.data) #data is JSON data send from postman
    if serializer.is_valid(): #pass to serializers for validation
        serializer.save() #calls create and save to database
        return Response(
            {"message":"User Registerd Successfully"}, 
            status=status.HTTP_201_CREATED
        )
    return Response( #if validation fails
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )