from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='index'),
    path('profile/',views.profile,name='profile'),
    path('list/',views.list_available,name='list'),
    path('signup/', views.SignUp.as_view(),name='signup'),
    path('blank/',views.blankView,name='blank'),
]