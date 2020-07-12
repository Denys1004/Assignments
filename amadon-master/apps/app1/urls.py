from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy_product', views.buy_product),
    path('checkout', views.checkout)
]