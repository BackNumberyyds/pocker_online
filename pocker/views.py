from django.shortcuts import render

# Create your views here.


def tolobby(request):
    return render(request, 'pocker/lobby.html')


def room(request, room_name):
    return render(request, "pocker/room.html", {"room_name": room_name})
