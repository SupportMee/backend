from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

from .models import Hueca, Menu, Image
from .serializers import HuecaSerializer, MenuSerializer, ImageSerializer

#IMAGES

# response  a single Image
@api_view(['GET','DELETE'])
def image(request, pk):
    data = generics.get_object_or_404(Image,id=pk)
    #data = Image.objects.get(hueca=hueca)
    if(request.method=='GET'):
        serializer = ImageSerializer(data, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        data.delete()
        return Response('Item succsesfully delete!',status=status.HTTP_200_OK)  

# response  of  image
@api_view(['POST'])
def post_image(request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)  


# response list of images
@api_view(['GET'])
def images(request,hueca):
    data = Image.objects.filter(hueca=hueca).all()
    serializer = ImageSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


# response list of huecas
@api_view(['GET'])
def huecas(request):
    data = Hueca.objects.all()
    serializer = HuecaSerializer(data, many=True)
    return Response(serializer.data)


# response  a single hueca
@api_view(['GET'])
def hueca(request, pk):
    data = Hueca.objects.get(id=pk)
    serializer = HuecaSerializer(data, many=False)
    return Response(serializer.data)




