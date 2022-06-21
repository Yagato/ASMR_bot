import discord
import os
from yt import *
from dotenv import load_dotenv
from discord.ext import tasks

client = discord.Client()
        
@client.event
async def on_ready():
    check_channels.start()

@tasks.loop(seconds=60)
async def check_channels():
    user = await client.fetch_user(os.getenv('USER_ID'))

    latest_video_title = get_latest_video_title('UUvaTdHTWBGv3MKj3KVqJVCw')

    if 'ASMR' in latest_video_title:
        latest_video_link = get_latest_video_link('UUvaTdHTWBGv3MKj3KVqJVCw')
        bot_message = f'New video! \n{latest_video_link}'
        async for messages in user.history(limit=1):
            if(bot_message != messages.content):
                await user.send(bot_message)
            else:
                print("Duplicate message")
    else:
        print('Not ASMR')

load_dotenv()
client.run(os.getenv('TOKEN'))