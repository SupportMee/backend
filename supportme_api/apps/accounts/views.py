from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.
from django.contrib.auth.models import User
from .serializers import UserSerializer
# response list of likes


@api_view(['POST'])
def login(request):
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
    return Response(data)
    

@api_view(['POST'])
def createUser(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
    
	return Response(serializer.data)
    

@api_view(['GET'])
def users(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response(serializer.data)


'''
@api_view(['POST'])
def createUser(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
        serializertok = ObtainAuthToken.serializer_class(data=request.data, context={'request': request})
        serializertok.is_valid(raise_exception=True)
        user = serializertok.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
            'username': user.username,
            'id': user.pk,
            'email': user.email
        }

        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

'''