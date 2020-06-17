from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.playerprofile, name='playerprofile'),
]
