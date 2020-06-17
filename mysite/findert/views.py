from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from findert.models import Player


# Create your views here.

def index(request):
    print(request)
    return render(request, 'findert/wrapper.html', )


def create(request):
    pass
    # if request.method == "POST":
    #     data = Player()
    #     data.player_email = request.POST.get("email")
    #     data.player_name = request.POST.get("username")
    #     data.player_password = request.POST.get("password")
    #     data.faceit_link = request.POST.get("faceit")
    #     data.steam_link = request.POST.get("steam")
    #     data.Rank_choise = request.POST.get("rank")
    #     data.Skill_choise = request.POST.get("skill")
    #     data.MainRole_choise = request.POST.get("main_role")
    #     data.TacticalRole_choise = request.POST.get("tactical_role")
    #     data.Region_choise = request.POST.get("region")
    #     data.Goal_choise = request.POST.get("goal")
    #     data.Country_choise = request.POST.get("country")
    #     data.Language_choise = request.POST.get("language")
    #     data.save()
    #     print(data)
    # return HttpResponseRedirect("/")
