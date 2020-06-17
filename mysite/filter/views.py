from django.shortcuts import render
from findert.models import Player
from django.http import HttpResponseRedirect
# Create your views here.


def filter(request):
    if request.method == "POST":
        Language = request.POST.get("language")
        Skill_lvl = request.POST.get("skill")
        Rank = request.POST.get("rank")
        Main_role = request.POST.get("main_role")
        try:
            play = Player.objects.filter(player_language__exact=Language, player_skill__exact=Skill_lvl, player_rank__exact=Rank, player_mainrole__exact=Main_role) [:3]
        except Player.DoesNotExist:
            user = None
    return render(request, "findert/players.html", {'play': play})