from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('findert.urls')),
    path('teams/', include('teams.urls')),
    path('teamprofile/', include('teamprofile.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('players/', include('players.urls')),
    path('login/playerprofile/', include('playerprofile.urls')),
    path('players/players/filter/', include('filter.urls')),
    path('createTeam/', include('createTeam.urls')),
]
