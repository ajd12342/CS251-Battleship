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

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        pass
        # text_data_json = json.loads(text_data)
        #
        # # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'from': text_data_json['from'],
        #         'to': text_data_json['to'],
        #         'purpose': text_data_json['purpose']
        #     }
        # )

    # Receive message from room group
    async def chat_message(self, event):
        # if event['to']==self.user.username:
        #     print("Works")

        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
