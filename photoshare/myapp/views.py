from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {
        'categories':categories, 
        'photos':photos,
    }
    return render(request, 'pages/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo':photo,
    }
    return render(request, 'pages/view.html', context)

def addPhoto(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'pages/add.html', context)