from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html', status=200, context={ 'nome':'Wellington'})
