from django.urls import path
from . import views

urlpatterns = [
	path('likes/<int:hueca>/', views.likes, name="likes-hueca-list"),
	path('like/<int:hueca>/<int:user>/', views.like, name="like-hueca-user"),
	#path('categories/', views.categories, name="categories-list"),
]
