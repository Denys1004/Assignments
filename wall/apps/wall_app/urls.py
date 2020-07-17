from django.urls import path
from . import views


urlpatterns = [
    path('', views.wall),
    path('create_message', views.create_message),
    path('add_comment/<int:id>', views.add_comment),
    path('like/<int:id>', views.add_like),
    path('unlike/<int:id>', views.remove_like),
    path('delete_message/<int:id>', views.delete_message),
    path('delete_user/<int:id>', views.delete_user),
]
