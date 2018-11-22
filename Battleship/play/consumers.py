from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import Game,PlayerPieces
from picklefield.fields import PickledObjectField
class SubmitConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.user=self.scope["user"]
        self.room_name = "placing"
        self.room_group_name = 'chat_placing'
        self.game_id=None
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        print(self.user.username,"Left")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'purpose': 'Left Game',
                'game_id': self.game_id,
                'from': self.user.username
            })
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    # Receive message from room group
    async def chat_message(self, event):
        print(event)
        print(self.game_id)
        if(event['purpose']=='Set Game ID' and self.user.username==event['from']):
            self.game_id=event['game_id']
        else:
            if(event['game_id']==self.game_id):
                if(event['purpose']=='Left Game'):
                    # g=Game.objects.get(pk=event['game_id'])
                    # p1=g.player1Pieces
                    # p2=g.player2Pieces
                    # g.delete()
                    # p1.delete()
                    # p2.delete()
                    print(event)
                    print("Left")
                    await self.send(text_data=json.dumps(event))
                if(event['purpose']=='Placing done'):
                    g=Game.objects.get(pk=event['game_id'])
                    if(self.user.username==event['from']):

                        if(g.player1.username==event['from']):
                            print("enter")
                            g.player1Placed=True
                            g.player1Pieces.noOfSunkShips=0
                            g.player1Pieces.squares=event['squares']
                            g.player1Pieces.iOfSquaresOfType=event['iOfSquaresOfType']
                            g.player1Pieces.jOfSquaresOfType=event['jOfSquaresOfType']
                            g.player1Pieces.squaresLeft=[0,2,3,1,1,1]
                            g.player1Pieces.whichShipsSunk=[False,False,False,False,False,False]
                            g.player1Pieces.save()
                            g.save()
                        if (g.player2.username == event['from']):
                            g.player2Placed = True
                            g.player2Pieces.noOfSunkShips = 0
                            g.player2Pieces.squares = event['squares']
                            g.player2Pieces.iOfSquaresOfType = event['iOfSquaresOfType']
                            g.player2Pieces.jOfSquaresOfType = event['jOfSquaresOfType']
                            g.player2Pieces.squaresLeft = [0, 2, 3, 1, 1, 1]
                            g.player2Pieces.whichShipsSunk = [False, False, False, False, False, False]
                            g.player2Pieces.save()
                            g.save()
                    if(g.player1Placed and g.player2Placed):
                        print("Entered final check")
                        print(event['game_id'])
                        await self.channel_layer.group_send(
                            self.room_group_name,
                            {
                                'type': 'chat_message',
                                'purpose': 'Complete',
                                'game_id': event['game_id']
                            }
                        )
                if(event['purpose']=='Complete'):
                    await self.send(text_data=json.dumps(event))


class GameConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.user=self.scope["user"]
        self.room_name = "game"
        self.room_group_name = 'chat_game'
        self.game_id=None
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        print(self.user.username,"Left")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'purpose': 'Left Game',
                'game_id': self.game_id,
                'from': self.user.username
            })
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    # Receive message from room group
    async def chat_message(self, event):
        #print(event)
        if(event['purpose']=='Set Game ID' and self.user.username==event['from']):
            self.game_id=event['game_id']
            await self.send(text_data=json.dumps(gameState(self.game_id,self.user.username)))
        elif(self.game_id==event['game_id']):
            if(event['purpose']=='Left Game'):
            # g=Game.objects.get(pk=event['game_id'])
            # p1=g.player1Pieces
            # p2=g.player2Pieces
            # g.delete()
            # p1.delete()
            # p2.delete()
                print(event)
                print("Left")
                await self.send(text_data=json.dumps(event))


def gameState(game_id,from_username):
    g=Game.objects.get(pk=game_id)
    return {
                'type': 'chat_message',
                'from': from_username,
                'purpose': 'Initialize Game',
                'p1': g.player1.username,
                'p2': g.player2.username,
                'p1squares': g.player1Pieces.squares,
                'p1iOfSquaresOfType': g.player1Pieces.iOfSquaresOfType,
                'p1jOfSquaresOfType': g.player1Pieces.jOfSquaresOfType,
                'p1noOfSunkShips':g.player1Pieces.noOfSunkShips,
                'p1squaresLeft':g.player1Pieces.squaresLeft,
                'p2squares': g.player2Pieces.squares,
                'p2iOfSquaresOfType': g.player2Pieces.iOfSquaresOfType,
                'p2jOfSquaresOfType': g.player2Pieces.jOfSquaresOfType,
                'p2noOfSunkShips': g.player2Pieces.noOfSunkShips,
                'p2squaresLeft': g.player2Pieces.squaresLeft,
                'activePlayerIs1':g.activePlayerIs1,
                'game_id': game_id,
            }







