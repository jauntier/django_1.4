from django.shortcuts import render
from .models import Post

# Create your views here.
# def home(request):
#     return render(request, 'home.html')


def home(request):
    context = {
        "title": "Home page",
        "description": "Welcome to the home page!!",
        
        
    }
    return render(request, 'home.html', context)



def about(request):
    context = {
        "title": "About page",
        "description": "Welcome to the about page"
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "title": "Contact page",
        "description": "Welcome to the contact page"
    }
    return render(request, 'contact.html', context)


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})