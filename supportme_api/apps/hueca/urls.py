from django.urls import path
from . import views

urlpatterns = [
	path('huecas/', views.huecas, name="huecas-list"),
	path('hueca/<int:pk>/', views.hueca, name="hueca-single"),
	path('image/<int:hueca>/', views.image, name="image-hueca"),
]
