from django.shortcuts import render
from findert.models import Team, Player
from django.http import HttpResponseRedirect
# Create your views here.

def createTeam(request):
    if request.POST.get('csrfmiddlewaretoken'):
        data = Team()
        data.team_name = request.POST.get("name")
        data.team_goal = request.POST.get("goal")
        data.team_country = request.POST.get("country")
        data.team_language = request.POST.get("language")
        data.team_region = request.POST.get("region")
        Player.team_id = data.id
        data.save()
        return HttpResponseRedirect("/")
    return render(request, 'findert/createTeam.html')
