"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app1 import views
from django.contrib import admin
from django.urls import path
from app1.views import python,java,php
from app2.views import home,course,contact,About
urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/",views.index),
    path("python/",python),
    path("php/",php),
    path("java/",java),
    path("home/",home),
    path("course/",course),
    path("contact/",contact),
    path("about/",About)

]
