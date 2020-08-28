from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City, Category
from .serializers import CitySerializer, CategorySerializer

# response list of cities
@api_view(['GET'])
def cities(request):
    tasks = City.objects.all().order_by('-name')
    serializer = CitySerializer(tasks, many=True)
    return Response(serializer.data)

# response list of categories
@api_view(['GET'])
def categories(request):
    tasks = Category.objects.all().order_by('-name')
    serializer = CategorySerializer(tasks, many=True)
    return Response(serializer.data)

# response a single city
@api_view(['GET'])
def city(request, pk):
    tasks = City.objects.get(id=pk)
    serializer = CitySerializer(tasks, many=False)
    return Response(serializer.data)

# response a single category
@api_view(['GET'])
def category(request, pk):
    tasks = Category.objects.get(id=pk)
    serializer = CategorySerializer(tasks, many=False)
    return Response(serializer.data)



"""
@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

"""