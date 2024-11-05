from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery' ),
    path('addphoto/', views.addPhoto, name='add_photo' ),
    path('viewphoto/<str:pk>/', views.viewPhoto, name='view_photo' ),
    
    # authentication
    path('login/', views.loginPage, name='login_page'), #login url
    path('logout/', views.logoutPage, name='logout_page'), #logout url
    path('register/', views.registerPage, name='register_page') #register url
]
