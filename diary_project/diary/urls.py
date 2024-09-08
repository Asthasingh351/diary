from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_entry_list, name='diary_entry_list'),
    path('add/', views.diary_entry_add, name='diary_entry_add'),
    path('edit/<int:pk>/', views.diary_entry_edit, name='diary_entry_edit'),
    path('delete/<int:pk>/', views.diary_entry_delete, name='diary_entry_delete'),
]
