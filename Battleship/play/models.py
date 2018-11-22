from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
# Create your models here.
class PlayerPieces(models.Model):
    noOfSunkShips = models.IntegerField()
    # 3 of 1*1, 2 of 2*1, 1 of 4*1, 1 of 3 square L, 1 of 5 square T
    squares = PickledObjectField()
    # 0 not filled, 1 filled, 2 clicked
    iOfSquaresOfType= PickledObjectField()
    jOfSquaresOfType= PickledObjectField()
    squaresLeft=PickledObjectField()
    whichShipsSunk=PickledObjectField()

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2')
    player1Pieces = models.OneToOneField(PlayerPieces, on_delete=models.CASCADE, related_name='player1Pieces')
    player2Pieces = models.OneToOneField(PlayerPieces,on_delete=models.CASCADE,related_name='player2Pieces')
    player1Placed=models.BooleanField()
    player2Placed=models.BooleanField()
    activePlayerIs1=models.BooleanField()