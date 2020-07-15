from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('create_message', views.create_message),
    path('banana', views.banana),
]
