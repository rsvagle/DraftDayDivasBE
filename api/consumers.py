import os
import django
import time

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'draft_day_divas.settings')
django.setup()

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
from channels.db import database_sync_to_async
from django.shortcuts import get_object_or_404
from .models import FantasyDraft
from .serializers import FantasyDraftSerializer
import json

class DraftConsumer(AsyncWebsocketConsumer):
    # connect a user
    async def connect(self):
        try:
            token_key = self.scope['query_string'].decode().split('token=')[1] # or from headers
            token = await self.get_token(token_key)
            user = token.user
            self.scope['user'] = user
        except Token.DoesNotExist:
            raise DenyConnection("Invalid token")
        except Exception as e:
            raise DenyConnection("Authentication failed")

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"draft_{self.room_name}"

        # Ensure user has permission to join this room
        if not await self.user_can_join(self.room_name):
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Wait a bit then announce the user has joined
        time.sleep(2)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": "System",
                "message": user.username + " joined the draft!",
            }
        )

    # Disconnect a user
    async def disconnect(self, close_code):
        user = self.scope['user']
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # Wait a bit then announce the user has left
        time.sleep(2)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": "System",
                "message": user.username + " has left the draft!",
            }
        )

    # Receive user input
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

    # 
    # Methods
    #

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "type": event["type"],
            "username": event["username"],
            "text": event["message"],
        }))

    
    async def send_lobby_state(self):
        # Send the updated lobby state """
        lobby_state = await self.get_lobby_state(self.room_name)
        await self.send(text_data=json.dumps({
            "type": "draft_state",
            "state": lobby_state
    }))

    @database_sync_to_async
    def get_lobby_state(self, draft_id):
        # Fetch lobby state (mocked for now, ideally from DB/cache) """
        draft_instance = get_object_or_404(FantasyDraft, id=draft_id)
        serializer = FantasyDraftSerializer(draft_instance)
        return serializer.data
    
    async def make_draft_selection(self, text_data):
        # check it's the user's turn

        # check that this player hasn't been selected yet

        # pick the player

        data = json.loads(text_data)
        username = data['username']
        player_name = data['player']['player']
        pick = data['pick']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": username,
                "message": 'Drafted:' + player_name + ' at pick ' + str(pick),
            }
        )

    # 
    # Auth helpers
    # 
    @database_sync_to_async
    def get_token(self, token_key):
        return Token.objects.select_related('user').get(key=token_key)

    @database_sync_to_async
    def user_can_join(self, draft_id):
        draft_instance = get_object_or_404(FantasyDraft, id=draft_id)
        user = self.scope["user"]

        # Check if any draft_team has this user
        if draft_instance.draft_teams.filter(user=user).exists():
            return True

        return False