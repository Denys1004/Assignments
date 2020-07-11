from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_form', views.process_form),
    path('destroy/<int:id>', views.destroy_or_cancel),
    path('comments/<int:id>', views.comments),
    path('courses/<int:id>/comment', views.create_comment),
    path('remove/<int:id>', views.remove)
]
