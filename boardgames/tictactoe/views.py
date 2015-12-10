from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {'message': 'hi, friom tictactoe!'})


from rest_framework import viewsets
from rest_framework import permissions
from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Game.objects.all()
    # Some change in branch 2
    serializer_class = GameSerializer