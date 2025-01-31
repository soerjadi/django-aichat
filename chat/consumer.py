import json
from channels.generic.websocket import AsyncWebsocketConsumer
from openai import OpenAI
import os


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": "soerja",
            },
        )

        client = OpenAI(
            organization=os.getenv('OPENAI_ORG'),
            project=os.getenv('OPENAI_PROJECT'),
            api_key=os.getenv('OPENAI_API_KEY')
        )

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": message}
            ]
        )

        response = completion.choices[0].message.content

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": response,
                "username": "Assistant",
            },
        )

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

    pass
