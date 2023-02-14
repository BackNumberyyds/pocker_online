from django.urls import path
from . import views

urlpatterns = [
    path('', views.tolobby),
    path("<str:room_name>/", views.room, name="room"),
]
