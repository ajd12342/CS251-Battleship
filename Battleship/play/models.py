from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
# Create your models here.
class PlayerPieces(models.Model):
    noOfSunkShips = models.IntegerField()
    # 3 of 1*1, 2 of 2*1, 1 of 4*1, 1 of 3 square L, 1 of 5 square T
    positions = PickledObjectField()
    # String corr to shape : (set of (coordinates,hit) , no of squares left)
    whichShipsSunk=PickledObjectField()

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2')
    player1Pieces = models.ForeignKey(PlayerPieces, on_delete=models.CASCADE, related_name='player1Pieces')
    player2Pieces = models.ForeignKey(PlayerPieces,on_delete=models.CASCADE,related_name='player2Pieces')
    player1Forbidden = PickledObjectField()  # 2D Grid
    player2Forbidden = PickledObjectField()  # 2D Grid
    activePlayerIs1=models.BooleanField()
    gameID=models.BigIntegerField()