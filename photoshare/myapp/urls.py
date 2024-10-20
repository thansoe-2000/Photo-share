from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery' ),
    path('addphoto/', views.addPhoto, name='add_photo' ),
    path('viewphoto/<str:pk>/', views.viewPhoto, name='view_photo' ),
]
