from django.urls import path

from . import views

urlpatterns = [
    path('place/<room_name>/', views.placing, name='place'),
]