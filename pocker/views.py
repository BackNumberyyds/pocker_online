from django.shortcuts import render

# Create your views here.


def tolobby(request):
    return render(request, 'pocker/lobby.html')
