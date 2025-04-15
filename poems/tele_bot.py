from telethon import TelegramClient, events
import requests
import json
import base64
from io import BytesIO

API_ID = '23842514'
API_HASH = '75b59dd4a465ac78e757681903966e44'
CHANNEL = 'https://t.me/tvorha_natura'
DJANGO_API_URL = 'https://yourwebsite.com/api/receive_poem/'

client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL))
async def new_message_handler(event):
    poem_text = event.message.text or ""
    image_data = None

    # Якщо є фото в повідомленні
    if event.message.photo:
        img = await event.message.download_media(BytesIO())
        image_data = f"data:image/jpeg;base64,{base64.b64encode(img.getvalue()).decode()}"

    data = {'title': 'Нове надходження', 'text': poem_text, 'image': image_data}

    response = requests.post(DJANGO_API_URL, json=data)
    print(response.json())  # Для дебагу

client.start()
client.run_until_disconnected()
