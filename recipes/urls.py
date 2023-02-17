
from django.contrib import admin
from django.urls import path

from recipes.views import home

urlpatterns = [
    path('', home),

]
