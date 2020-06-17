from django.shortcuts import render
from findert.models import Player


# Create your views here.

def playerprofile(request):
    if request.method == "GET":
        UserPassword = request.GET.get("password")
        Login = request.GET.get("login")
        try:
            player = Player.objects.get(player_password__exact=UserPassword, player_email__exact=Login)
        except Player.DoesNotExist:
            user = None
        return render(request, "findert/playerprofile.html", {'Player': player})
