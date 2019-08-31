from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),
    path('dashboard/<int:user_id>/create_note/', views.create_note, name='create_note'),
    path('dashboard/<int:user_id>/<int:note_id>/update_note/', views.update_note_view, name='update_note'),
    path('dashboard/<int:user_id>/<int:note_id>/delete_note', views.delete_note, name='delete_note'),
    path('dashboard/<int:user_id>/profile', views.user_profile, name='user_profile'),
]