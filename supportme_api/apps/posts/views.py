from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Like, Rating, Comment
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer


from apps.hueca.models import Hueca
from django.contrib.auth.models import User

# response list of likes
@api_view(['GET'])
def likes(request, hueca):
    data = Like.objects.filter(hueca=hueca).all()
    serializer = LikeSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# response  of like
@api_view(['GET','DELETE'])
def like(request, hueca, user):
    #data = Like.objects.get(hueca=hueca,user=user)
    data = generics.get_object_or_404(Like,hueca=hueca,user=user)
    if(request.method=='GET'):
        serializer = LikeSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        data.delete()
        return Response('Item succsesfully delete!',status=status.HTTP_200_OK)    

# response  of like
@api_view(['POST'])
def post_like(request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

#RATING SOLO SE PUEDE HACER POST Y GET
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

# response  of scores
@api_view(['POST'])
def post_rating(request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


#COMMENTS
# response list of comments
@api_view(['GET'])
def comments(request, hueca):
    data = Comment.objects.filter(hueca=hueca).all().order_by('created_on')
    serializer = CommentSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# response  of comments
@api_view(['DELETE'])
def comment(request,pk):
    data = generics.get_object_or_404(Comment,id=pk)
    data.delete()
    return Response('Item succsesfully delete!',status=status.HTTP_200_OK)  

# response  of comments
@api_view(['POST'])
def post_comment(request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

