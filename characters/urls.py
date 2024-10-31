# characters/urls.py
from django.urls import path

from characters import views

urlpatterns = [
    path('', views.characters_list, name='home'),
    path('characters', views.characters_list, name='characters_list')
]

