from channels.generic.websocket import AsyncWebsocketConsumer
import json
from play.models import Game,PlayerPieces
from django.contrib.auth.models import User
import os
class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.user=self.scope["user"]
        self.room_name = "list"
        self.room_group_name = 'chat_list'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'logged_username':self.user.username,
                'is_logged_in':True
            }
        )
        await self.accept()
        self.user.profile.isAvailable=True
        self.user.profile.save()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'logged_username': self.user.username,
                'is_logged_in':False
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        self.user.profile.isAvailable = False
        self.user.profile.save()

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
        if('logged_username' in event):
            await self.send(text_data=json.dumps(event))
        if('purpose' in event and (event['to']==self.user.username or event['from']==self.user.username)):
            if event['to']==self.user.username and event['to'] != event['from']:
                if(event['purpose']=='Accept_Request'):
                    g=Game.objects.create(player1=self.user,
                                          player2=User.objects.get(username=event['from']),
                                          player1Pieces=PlayerPieces.objects.create(
                                              noOfSunkShips=0,
                                          ),
                                          player1Score=0,
                                          player2Pieces=PlayerPieces.objects.create(
                                              noOfSunkShips=0),
                                          activePlayerIs1=True,
                                          player1Placed=False,
                                          player2Placed=False,
                                          player2Score=0,
                                          )
                    event['game_id'] = g.id
                await self.send(text_data=json.dumps(event))
        # if event['to']==self.user.username:
        #     print("Works")
