import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'draft_day_divas.settings')
django.setup()

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
from channels.db import database_sync_to_async
import json

class DraftConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            token_key = self.scope['query_string'].decode().split('token=')[1] # or from headers
            token = await self.get_token(token_key)
            user = token.user
            self.scope['user'] = user
        except Token.DoesNotExist:
            print("Token not found")
            raise DenyConnection("Invalid token")
        except Exception as e:
            print(f"Authentication failure: {e}")
            raise DenyConnection("Authentication failed")

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"draft_{self.room_name}"

        # Ensure user has permission to join this room
        if not await self.user_can_join():
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Ensure only authenticated users can send messages
        if self.scope["user"].is_authenticated:
            username = self.scope["user"].username
            message_type = data.get('type')

            if message_type == 'chat_message':
                message = data['text']
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "chat_message",
                        "username": username,
                        "message": message,
                    }
                )
            elif message_type == 'state_request':
                await self.send_lobby_state()
            elif message_type == 'draft_pick':
                await self.make_draft_selection(text_data)

    async def user_can_join(self):
        # """
        # Check if the authenticated user is allowed to join the draft room.
        # """
        # Implement your logic here (e.g., checking if they are part of the draft)
        return True  # Replace with actual permission checks

    # Methods
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "type": event["type"],
            "username": event["username"],
            "text": event["message"],
        }))

    async def send_lobby_state(self):
        # Send the updated lobby state """
        lobby_state = await self.get_lobby_state()
        await self.send(text_data=json.dumps({
            "type": "lobby_state",
            "state": lobby_state
    }))

    async def get_lobby_state(self):
        # Fetch lobby state (mocked for now, ideally from DB/cache) """
        return {"players": ["user1", "user2"], "status": "active"}
    
    async def make_draft_selection(self, text_data):
        data = json.loads(text_data)
        username = data['username']
        player_name = data['player']['player']
        pick = data['pick']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": username,
                "message": 'Drafted:' + player_name + 'at pick ' + str(pick),
            }
        )

    @database_sync_to_async
    def get_token(self, token_key):
        return Token.objects.select_related('user').get(key=token_key)