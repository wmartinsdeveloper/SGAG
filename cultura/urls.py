
from django.urls import path
from . import views

app_name = 'cultura'

urlpatterns = [
    path('', views.homecultura, name="homecultura"),
    path('inserir/', views.cadastrocultura, name="cadastrocultura"),
]