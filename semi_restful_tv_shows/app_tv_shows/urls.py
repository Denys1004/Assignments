from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.add_new_show),
    path('process_new_show', views.process_new_show),
    path('shows/<int:id>', views.show_one_tvshow),
    path('edit/<int:id>', views.edit),
    path('update', views.update),
    path('delete/<int:id>', views.delete)
]



























