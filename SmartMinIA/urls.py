from django.contrib import admin
from django.urls import  path
from .views import index, usersprofile, faq, login, register, contacto, escaneos, incidentes, trabajadores

urlpatterns = [
    path('', index, name="index"),
    path('usersproile', usersprofile, name="users-profile"),
    path('faq', faq, name="pages-faq"),
    path('login', login, name="pages-login"),
    path('register', register, name="pages-register"),
    path('contacto', contacto, name="pages-contact"),
    path('escaneos', escaneos, name="escaneos"),
    path('trabajadores', trabajadores, name="trabajadores"),
    path('incidentes', incidentes, name="incidentes"),

]
