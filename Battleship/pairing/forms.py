from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget
from django.db.models.functions import datetime
from .models import Profile

class CustomSignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=True)
    location = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True,widget=SelectDateWidget(years=range(1900,datetime.datetime.today().year+10)))

    class Meta:
        model = User
        fields=['username']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(CustomSignUpForm, self).save(commit=True)
        user.profile.bio=self.cleaned_data['bio']
        user.profile.location=self.cleaned_data['location']
        user.profile.birth_date=self.cleaned_data['birth_date']
        user.profile.save()
        return user
