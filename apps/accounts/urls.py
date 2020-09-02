from django.urls import path
from . import views

urlpatterns = [
	path('users', views.users, name="users-list"),
	path('login', views.login, name="login-user"),
	path('signup', views.createUser, name="registrer-user"),
	path('logout/<int:user>', views.logout, name="cerrar-session-user"),
	path('delete/<int:user>', views.delete_account, name="delete-account-user"),

]
