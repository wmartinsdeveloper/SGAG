from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.
def cultura (request):
    return render(request,'cultura/pages/cultura.html',status=201, context={'name':'Wellington'})


def cadastrocultura (request):
      return render(request,'cultura/pages/CadastroCultura.html',status=201)

