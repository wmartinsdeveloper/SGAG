from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import path,reverse
from .forms import culturaform
from .models import cultura as culturamodel

# Create your views here.
def homecultura (request):
    if request.method == "GET":
        listacultura = culturamodel.objects.all()   
        return render(request, 'cultura/pages/cultura.html', context={'listacultura': listacultura})
    

def cadastrocultura (request):
    if request.method == "POST":
        POST =request.POST
        request.session['cultura_form_data'] = POST
        form = culturaform(POST)
        if form.is_valid():
            form.save()  
            del(request.session['cultura_form_data'])   
            return redirect(reverse('cultura:homecultura'))
        else: 
            form = culturaform(request.session.get('cultura_form_data',None))
            return render(request, 'cultura/pages/CadastroCultura.html',context={"form": form})
    else:
        form = culturaform()
        return render(request, 'cultura/pages/CadastroCultura.html',context={"form": form})
    




