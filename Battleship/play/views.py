from django.http import *
from django.urls import reverse
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def placing(request, room_name):
    return render(request,'play/placing.html',{'room_name': mark_safe(room_name)})
