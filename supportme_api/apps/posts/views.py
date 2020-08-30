from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Like, Rating, Comment
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer


from apps.hueca.models import Hueca
from django.contrib.auth.models import User

# response list of likes

@api_view(['GET'])
def likes(request, hueca):
    data = Like.objects.filter(hueca=hueca).all().count()
    serializer = LikeSerializer(data, many=True)
    return Response(serializer.data)

# response  of like
@api_view(['GET'])
def like(request, hueca, user):
    data = Like.objects.get(hueca=hueca,user=user)
    serializer = LikeSerializer(data, many=False)
    return Response(serializer.data)


# response list of scores
@api_view(['GET'])
def ratings(request, hueca):
    data = Rating.objects.filter(hueca=hueca).all()
    serializer = RatingSerializer(data, many=True)
    return Response(serializer.data)


# response  list of scores
@api_view(['GET'])
def rating(request, hueca, user):
    data = Rating.objects.get(hueca=hueca, user=user)
    serializer = RatingSerializer(data, many=False)
    return Response(serializer.data)
