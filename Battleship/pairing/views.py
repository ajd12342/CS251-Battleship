from django.http import *
from django.urls import reverse
from .models import *
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.models import Permission, User
# Create your views here.
def index(request):
	if(not request.user.is_authenticated):
		return HttpResponseRedirect('/accounts/login/')
	else:
		return HttpResponseRedirect('/pairing/profile/')

def profile(request):
	return render(request,'pairing/profile.html',{})

def list(request):
	return HttpResponse("This should show a list of logged in players")