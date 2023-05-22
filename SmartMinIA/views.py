from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')

def usersprofile(request):

    return render(request, 'users-profile.html')

def faq(request):

    return render(request, 'pages-faq.html' )

def login(request):

    return render(request, 'pages-login.html')

def register(request):

    return render(request, 'pages-register.html')

def contacto(request):

    return render(request, 'pages-contact.html')