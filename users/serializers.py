from rest_framework import serializers #import serializers from DRF
from django.contrib.auth.models import User #import model
#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True) #password never be send back in response
    class Meta: #config class inside serializers
        model=User #this serializers is for user table
        fields=['username','email','password'] #which column should accept from postman
    def create(self,validated_data): #to saving new user
        #this create user with hashed password
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        ) #create_user() is special method that hashes the password , never user create() directly it will not hash password
        return user