from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    # photos = Photo.objects.all()
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
    if request.method == 'POST':
        data = request.POST
        photo = request.FILES.get('photo')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            photo = photo,
            
        )
        return redirect(gallery)
        
    context = {
        'categories':categories,
    }
    return render(request, 'pages/add.html', context)