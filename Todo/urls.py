
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('views/<int:id>', views.view, name="todo_view"),
    path('edit/<int:id>', views.edit, name="todo_edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('create/', views.create, name="todo_create")
]
