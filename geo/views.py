#-*- coding: utf-8 -*-

from django.shortcuts import render
from datetime import datetime
from .forms import *


# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the geo app index.")

def post_new(request):
    
    
    if request.method == "POST":
        form = PostHornetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_dtime = timezone.now()
            post.save()
            msg1="Trugarez !"
            msg2="Merci de votre participation"
            return render(request, 'geo/geothanks.html',{'msgligne2':msg2, 'msgligne1':msg1})# page ok new entry , thanks ! 
        else:
            msg1=" -- Erreur d'envoi --"
            msg2="Veuillez svp corriger et renvoyer"
            return render(request, 'geo/geopost.html', {'msgligne2':msg2,'form': form,'msgligne1':msg1})
            #post=post 
    else :
        return geoh(request)
        
                
        #return render(request, 'geo/testarrival.html', {'form': form})
def post_first(request):
    
    if request.method == "POST":
        form = PostHornetForm(request.POST)
        msg1="Formulaire d'envoi express!"
        msg2="Veuillez svp confirmer l'observation"
        return render(request, 'geo/geopost.html', {'msgligne2':msg2,'form': form,'msgligne1':msg1})
    else :
        return geoh(request)
    
     
def geoh(request):
    
    form = PostHornetForm()
    #form.view_dtime = timezone.now()
    latti=4
    return render(request, 'geo/geoclean.html', {'form': form})

def geothanks(request):
    
 
    msg1="Trugarez !"
    msg2="Merci de votre participation"
    return render(request, 'geo/geothanks.html',{'msgligne2':msg2, 'msgligne1':msg1})# page ok new entry , thanks !



def date_actuelle(request):
    return render(request, 'geo/date.html', {'date': datetime.now()})


def controls(request):
    return render(request, 'geo/controlsSample.html')
