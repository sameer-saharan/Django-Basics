from django.urls import path
from .views import *

urlpatterns = [
    path('task/', view_task, name='view-task'),
    path('edit/<int:id>/', edit_task, name='edit-task'),
    path('delete/<int:id>/', delete_task, name='delete-task'),
    path('create/', create_task, name='create-task'),
]
