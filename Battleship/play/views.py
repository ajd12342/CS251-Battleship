from django.http import *
from django.urls import reverse
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from .models import Game

# Create your views here.
@login_required
def placing(request, room_name):
    p2=Game.objects.get(pk=room_name).player2
    p1=Game.objects.get(pk=room_name).player1
    if(p2!=request.user and p1!=request.user):
        return HttpResponseRedirect('/pairing/profile')
    # if(not(Game.objects.get(pk=room_name).player1==request.user or Game.objects.get(pk=room_name ==request.user))):
    #     return HttpResponseRedirect("pairing/profile")
    return render(request,'play/placing.html',{'room_name': mark_safe(room_name)})

@login_required
def game(request,room_name):
    p2 = Game.objects.get(pk=room_name).player2
    p1 = Game.objects.get(pk=room_name).player1
    if (p2 != request.user and p1 != request.user):
        return HttpResponseRedirect('/pairing/profile')
    return render(request,'play/game.html',{'room_name' : mark_safe(room_name)})

@login_required
def finish(request,room_name):
    g=Game.objects.get(pk=room_name)
    p2 = g.player2
    p1 = g.player1
    if (p2 != request.user and p1 != request.user):
        return HttpResponseRedirect('/pairing/profile')
    return render(request,'play/finish.html',{'room_name' : mark_safe(room_name),
                                              'winner': g.winner.username})

