from django.http import *
from django.urls import reverse
from .models import *
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.models import Permission, User
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	if(not request.user.is_authenticated):
		return HttpResponseRedirect('/accounts/login/')
	else:
		return HttpResponseRedirect('/pairing/profile/')

@login_required
def profile(request):
	return render(request,'pairing/profile.html',{})
	
@login_required
def list(request):
	return render(request,'pairing/list.html',{'profiles':Profile.objects.filter(isAvailable=True)})