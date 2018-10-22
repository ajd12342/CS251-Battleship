from django.http import *
from django.urls import reverse
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import Permission, User
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    return render(request, 'pairing/profile.html', {})

@login_required
def list_available(request):
    return render(request, 'pairing/list.html', {'users': User.objects.all()})

from .forms import CustomSignUpForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = CustomSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
