import os
import discord as ds
import youtube_dl
from random import choice

from discord.ext import commands
from dotenv import load_dotenv

#IMPORTANTE: para que el bot pueda leer la actividad de los members
intents = ds.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

fran = commands.Bot(command_prefix="fran ", description="Soy frantástico", intents=intents)

@fran.command()
async def load(ctx, extension):
    fran.load_extension(f"cogs.{extension}")

@fran.command()
async def unload(ctx, extension):
    fran.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        fran.load_extension(f"cogs.{filename[:-3]}")

#EVENTS
@fran.event
async def on_member_join(member):
    print(f'{member.name} has joined a server.')

@fran.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@fran.event
async def on_message(mssg):
    if mssg.content == "kill me":
        response = 'MAY DAY: se necesita un "fumeteo distorsionado" para este user'
        await mssg.channel.send(response)
    if mssg.content == "pls":
        response = 'Deje al dankmemer de una vez rey/reyna'
        await mssg.channel.send(response)
    await fran.process_commands(mssg)

fran.run(TOKEN)
