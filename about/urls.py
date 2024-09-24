from django.urls import path
from about.views import contato, sobre

urlpatterns = [
    path('contato', contato),
    path('sobre/', sobre),
]