from django.urls import path, include
from . import views

app_name = 'findert'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
