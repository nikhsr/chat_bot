import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client= discord.Client()
client=commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print("Thank you Have a nice day")
    awaigt client.change_presence(game=discord.Game(name="content_recommender"))

@client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg='Hello(0.author.mention) How are you today'.format(message)
        await client.send_message(message.channel,msg)
    if message.content.startswith('.bye'):
        msg='Goodbye(0.author.mention) hope to see you again:wave:'.format(message)
        await client.send_message(message.channel,msg)
client.run(os.getenv('Token')        
    
