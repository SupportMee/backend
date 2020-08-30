from django.urls import path
from . import views

urlpatterns = [
	path('users/', views.users, name="users-list"),
	#path('categories/', views.categories, name="categories-list"),
	path('login/', views.login, name="login-user"),
	path('registrer/', views.createUser, name="registrer-user"),

]
