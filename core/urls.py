"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.cultura, name='cultura')
Class-based views
    1. Add an import:  from other_app.views import cultura
    2. Add a URL to urlpatterns:  path('', cultura.as_view(), name='cultura')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'), name="home"),
    path('login/',include('login.urls'), name="login"),
    path('cultura/',include('cultura.urls'), name="cultura"),
    path('manejo/',include('manejo.urls'), name="manejo"),

]
