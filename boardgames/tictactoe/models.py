from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS_CHOICES=(
    ('A','Animal'),
    ('B','Ball'),
    ('C','China')
)


class Game(models.Model):
    first_player=models.ForeignKey(User, related_name="game_first_player")
    second_player=models.ForeignKey(User, related_name="game_second_player")
    next_to_move=models.ForeignKey(User, related_name="games_to_move")
    start_time=models.DateTimeField(auto_now_add=True)
    last_active=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=1, default='A', choices=STATUS_CHOICES,null=True )

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move (models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comment=models.CharField(max_length=200)
    Game=models.ForeignKey(Game)