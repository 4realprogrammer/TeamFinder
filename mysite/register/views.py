from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from findert.models import Player


def register(request):
    print(request)
    print(request.POST)
    if request.POST.get('csrfmiddlewaretoken'):
        data = Player()
        data.player_email = request.POST.get("email")
        data.player_name = request.POST.get("username")
        data.player_password = request.POST.get("password")
        data.faceit_link = request.POST.get("faceit")
        data.steam_link = request.POST.get("steam")
        data.player_rank = request.POST.get("rank")
        data.player_skill = request.POST.get("skill")
        data.player_mainrole = request.POST.get("main_role")
        data.player_tacticalrole = request.POST.get("tactical_role")
        data.player_region = request.POST.get("region")
        data.player_goal = request.POST.get("goal")
        data.player_country = request.POST.get("country")
        data.player_language = request.POST.get("language")
        data.save()
        return HttpResponseRedirect("/")
    return render(request, 'findert/register.html')