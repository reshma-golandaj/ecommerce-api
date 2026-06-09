#works as receptionist,when request comes in, it route to correct view
from django.urls import path #map url to view function
from rest_framework_simplejwt.views import (TokenObtainPairView, #built in login view, Automatically handles login and return JWT tokens
                                             TokenRefreshView)  # refresh token
from . import views
urlpatterns=[
    path('register/',views.register,name='register'), #go to register function
    path('login/',TokenObtainPairView.as_view(),name='login'), #goes to JWT's built in log in
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'), #refreshes expired tokens
]