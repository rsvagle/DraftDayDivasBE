from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods

# Login
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not user.check_password(password):
        return Response({"detail": "Incorrect password."}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

# Signup
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key, "user": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Test token
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Passed for {}".format(request.user.email))


# Get profile
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    # Access the user directly from request.user
    user = request.user

    # Now, you can use the user object to access any user information, such as username or user id
    user_id = user.id
    username = user.username
    email = user.email

    # Fetch additional user information from your database if needed
    # For example, you might have a UserProfile model associated with your User model
    # user_profile = UserProfile.objects.get(user=user)

    # Construct your response with the user information
    response_data = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "first_name": user.first_name,
        "last_name": user.last_name
        # Include other user details as needed
    }

    return Response(response_data)

# Save profile
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_user_profile(request):
    # Save/update profile logic
    user = User.objects.get(id=request.user.id)  # Example, adjust accordingly

    user.email = request.data['email']
    user.username = request.data['username']
    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    try:
        user.save()
    except:
        return Response(status=status.HTTP_409_CONFLICT)

    return Response(status=status.HTTP_200_OK)