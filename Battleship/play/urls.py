from django.urls import path

from . import views

urlpatterns = [
    path('place/<room_name>/', views.placing, name='place'),
    path('game/<room_name>',views.game,name='game'),
]