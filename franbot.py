import os
import discord as ds
import youtube_dl as yt
from random import choice

from discord.ext import commands
from dotenv import load_dotenv

#IMPORTANTE: para que el bot pueda leer la actividad de los members
intents = ds.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

fran = commands.Bot(command_prefix="fran ", description="Soy frantástico", intents=intents)

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


@fran.command(help='Tiro los mejores pls memes de la historia papA')
async def memes(ctx):
    quotes = [
        'pls ohno sleepyfran',
        'pls whodidthis chowfran',
        'pls stroke hi',
        'pls boo , hola batman'
    ]
    response = choice(quotes)
    await ctx.send(response)


@fran.command(aliases=['sleepyfran', 'sleepy'], help='Salen unas frases icónicas del sleepy con papas')
async def sleepy_hall_of_fame(ctx):
    quotes = [
        'uhh que dificil está levantarse de la cama',
        'me voy a merendar y vuelvo * nunca vuelve *',
        'que partida de mierda que estoy teniendo',
        'como cuesta levantarse chee'
    ]
    response = choice(quotes)
    await ctx.send(response)

@fran.command(name='fumeteo', help='Fran te da una mano para llegar al cielo')
async def fumeteo_time(ctx, url):
    response = "https://www.youtube.com/watch?v=Wv0OrskppsY"
    await ctx.send(response)

fran.run(TOKEN)
