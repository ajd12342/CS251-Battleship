from channels.generic.websocket import AsyncWebsocketConsumer
import json

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
            {
                'type': 'chat_message',
                'from': text_data_json['from'],
                'to': text_data_json['to'],
                'purpose': text_data_json['purpose']
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        ret={}
        if('purpose' in event):
            if event['to']==self.user.username and event['to'] != event['from']:
                ret=event
        # if event['to']==self.user.username:
        #     print("Works")
        else:
            # Send message to WebSocket
            ret=event

        await self.send(text_data=json.dumps(ret))
