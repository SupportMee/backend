from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Like, Rating, Comment
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer


from apps.hueca.models import Hueca
from apps.accounts.models import User

# response list of likes


@api_view(['GET'])
def likes(request, hueca):
    data = Like.objects.filter(hueca=hueca).all().count()
    serializer = LikeSerializer(data, many=True)
    return Response(data)

# response  of like
@api_view(['GET'])
def like(request, hueca, user):
    data = Like.objects.get(hueca=hueca,user=user)
    serializer = LikeSerializer(data, many=False)
    return Response(serializer.data)
