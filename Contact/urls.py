
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name="contact"),
    path('views/<int:id>', views.view, name='contact_view'),
    path('edit/<int:id>', views.edit, name='contact_edit'),
    path('create/', views.create, name='contact_create'),
    path('delete/<int:id>', views.delete, name='contact_delete'),
]
