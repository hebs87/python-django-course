from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dogs', views.dogs),
]
