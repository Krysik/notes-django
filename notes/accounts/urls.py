from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('accounts/register/', views.register_view, name='register'),
]