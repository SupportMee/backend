from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# Create your views here.
from django.contrib.auth.models import User
from .serializers import UserSerializer
# response list of likes


#login get token
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login(request):
    #request.data["password"] = make_password(request.data["password"])
    serializer = ObtainAuthToken.serializer_class(
        data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)

    data = {
        'token': token.key,
        'username': user.username,
        'user_id': user.pk,
        'email': user.email
    }
    return Response(data, status=status.HTTP_200_OK)
    

#registrer user
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def createUser(request):
    userExists=User.objects.filter(username=request.data["username"]).exists()
    if(userExists):
        msg={
            'error':"User already exists."
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    request.data["password"] = make_password(request.data["password"])
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#Get users
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAdminUser])
def users(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request,user):
    data = generics.get_object_or_404(Token,user=user)
    data.delete()
    msg={
        'msg':'Logout Successfully!'
    }
    return Response(msg,status=status.HTTP_200_OK)  


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_account(request,user):
    data = generics.get_object_or_404(User,user=user)
    data.delete()
    msg={
        'msg':'Delete Account Successfully!'
    }
    return Response(msg,status=status.HTTP_200_OK)