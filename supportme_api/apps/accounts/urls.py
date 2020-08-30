from django.urls import path
from . import views

urlpatterns = [
	path('users/', views.users, name="users-list"),
	#path('categories/', views.categories, name="categories-list"),
]
