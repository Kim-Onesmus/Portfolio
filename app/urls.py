from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('kimtech', views.KimTech, name='kimtech'),
    path('messanges', views.Messanges, name='messanges'),
]