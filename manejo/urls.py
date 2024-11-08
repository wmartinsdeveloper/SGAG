
from django.urls import path
from . import views


urlpatterns = [
    path('', views.manejo, name="manejo"),
]