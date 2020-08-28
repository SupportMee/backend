from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hueca, Menu, Image
from .serializers import HuecaSerializer, MenuSerializer, ImageSerializer


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


# response  a single Image
@api_view(['GET'])
def image(request, hueca):
    data = Image.objects.get(hueca=hueca)
    serializer = ImageSerializer(data, many=False)
    return Response(serializer.data)
