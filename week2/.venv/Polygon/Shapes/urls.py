from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('contact/',views.contact , name='contact'),
    path('about/', views.about, name='about')
]