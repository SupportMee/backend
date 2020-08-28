from django.urls import path
from . import views

urlpatterns = [
	path('likes/<int:hueca>/', views.likes, name="likes-hueca-list"),
	path('like/<int:hueca>/<int:user>/', views.like, name="like-hueca-user"),
	path('ratings/<int:hueca>/', views.ratings, name="ratings-hueca-list"),
	path('rating/<int:hueca>/<int:user>/', views.rating, name="rating-hueca-user"),
	#path('categories/', views.categories, name="categories-list"),
]
