# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    botiga = Botiga.objects.all()
    #carns = Carns.objects.all()
    #precuinats= Precuinats.objects.all()
    return render(request,'homepage.html',context={'botiga':botiga})

def carns(request):
    #botiga = Botiga.objects.all()
    #carns= Carns.objects.all()
    #precuinats= Precuinats.objects.all()
    return render(request,'carns.html')

def precuinats(request):
    #botiga = Botiga.objects.all()
    #carns= Carns.objects.all()
    #precuinats= Precuinats.objects.all()
    return render(request,'precuinats.html')
