from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator

from myapp.models import Photo
from myapp.models import Category
from . forms import *
# Create your views here.


# gallery

@login_required(login_url='login_page')
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
        paginator = Paginator(photos,6)
    
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        photos = Photo.objects.filter(category__name=category)
        paginator = Paginator(photos,6)
    
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    # photos = Photo.objects.all()
    
    # # pagination
    # photo = Photo.objects.all()
    # paginator = Paginator(photo,6)
    
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
  
    context = {
        'categories':categories, 
        'photos':photos,
        'page_obj':page_obj
    }
    return render(request, 'pages/gallery.html', context)

# view photos
@login_required(login_url='login_page')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo':photo,
    }
    return render(request, 'pages/view.html', context)

# create photo
@login_required(login_url='login_page')
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


# login
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('gallery')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_page')
        
            
    return render(request, 'authentication/login.html')

# logout
def logoutPage(request):
    logout(request)
    return redirect('login_page')

# register
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('gallery_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_page')
        context = {
            'form':form
        }
    return render(request, 'authentication/register.html', context)
        