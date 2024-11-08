from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.
def manejo (request):
    return render(request,'manejo/pages/CadastroManejo.html',status=201, context={'name':'Wellington'})
