from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('expenses', views.expenses, name='Wydatki'),
    path('planowanie', views.planowanie, name="Planowanie wydatków"),
    path('przychody', views.enter_the_income, name="Przychody w domowym budżecie"),
    path('name', views.get_name, name='Name'),
    path('kwota', views.get_amount, name='Formularz Wydatków'),
    path('przychody', views.enter_the_income, name="Przychody w domowym budżecie"),
    path('categories', views.enter_the_cost, name="Kategorie budżetu domowego"),
    path('wydatki', views.enter_the_cost, name="Kategorie budżetu domowego"),
    path('statement', views.display, name="Zestawienie"),
    path('kategoria', views.get_name1, name="Kategria"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)