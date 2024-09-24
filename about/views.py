from django.http import HttpResponse
from django.shortcuts import render

def contato(request):
    return render(request, 'about/contato.html', status=200)

def sobre(request):
    return render(request, 'about/sobre.html', status=200)
