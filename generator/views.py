from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(
                request,
                'generator/home.html')



def password(request):

    characters = list('abcdefghijklmnopqrtuvwxyz')
    
    if request.GET.get('uppercase'):
        # ovaj kod pod komentarom to je moj nacin, a ispod je nacin sa kursa
        # lowel_characters += list('ABCDEFGHIJKLMNOPQRTUVWXYZ')
        characters.extend(list('ABCDEFGHIJKLMNOPQRTUVWXYZ'))

    
    if request.GET.get('number'):
        # ovaj kod pod komentarom to je moj nacin, a ispod je nacin sa kursa
        # lowel_characters += list('1234567890')
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        # ovaj kod pod komentarom to je moj nacin, a ispod je nacin sa kursa
        # lowel_characters += list('./!?@#$%&*')
        characters.extend(list('./!?@#$%&*'))
    
    lenght = int(request.GET.get('length'))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):
    author = 'Aleksandar Lazarevic'
    return render(request, 'generator/about.html', {'author':author})