from django.shortcuts import render
from findert.models import Player
from django.http import HttpResponseRedirect
# Create your views here.

def player(request):
    return render(request, 'findert/players.html')