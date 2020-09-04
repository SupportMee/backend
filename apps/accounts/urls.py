from django.urls import path
from . import views

urlpatterns = [
	path('users', views.users, name="users-list"),
	path('login', views.login, name="login-user"),
	path('signup', views.createUser, name="registrer-user"),
	path('logout/<int:pk>', views.logout, name="cerrar-session-user"),
	path('delete/<int:pk>', views.deleteAccount, name="delete-account-user"),
	path('update/<int:pk>', views.updateUser, name="update-account-user"),

]
