from django.urls import path
from . import views

urlpatterns = [
	path('huecas/', views.huecas, name="huecas-list"),
	path('hueca/<int:pk>/', views.hueca, name="hueca-single"),

	path('images/<int:hueca>/', views.images, name="image-hueca-list"),
	path('image/<int:pk>/', views.image, name="image-hueca"),
	path('image/', views.post_image, name="image-post"),

    path('menus/<int:hueca>/', views.menus, name="menu-hueca-list"),
	path('menu/<int:pk>/', views.menu, name="menu-hueca"),
	path('menu/', views.post_menu, name="menu-post"),

]
