# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    botiga = Botiga.objects.all()
    return render(request,'homepage.html',context= {'botiga': botiga})

def carns(request):
    carns = Carns.objects.all()
    return render(request,'carns.html',context= {'carns': carns})

def precuinats(request):
    precuinats = Precuinats.objects.all()
    return render(request,'precuinats.html',context= {'precuinats': precuinats})
