import os
import discord as ds
from random import choice

from discord.ext import commands
from dotenv import load_dotenv

intents = ds.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

fran = commands.Bot(command_prefix="fran ", description="Soy frantástico")

@fran.event
async def on_member_join(member):
    channels = member.guild.text_channels
    print(channels)
#    await channel.send(
#        f'Que onda {member.name}? Bienvenido al server.\n El prefijo de este bot es "fran". Cualquier cosa que necesites llamame bb. <3'
#    )

@fran.event
async def on_message(mssg):
    if mssg.content == "kill me":
        response = 'MAY DAY: se necesita un "fumeteo distorsionado" para este user'
        await mssg.channel.send(response)
    await fran.process_commands(mssg)

@fran.command(name='memes', help='Tiro los mejores pls memes de la historia papA')
async def fran_service(ctx):
    quotes = [
        'pls ohno sleepyfran',
        'pls whodidthis chowfran',
        'pls stroke hi',
        'pls boo , hola batman'
    ]
    response = choice(quotes)
    await ctx.send(response)

@fran.command(name='sleepyfran', help='Salen unas frases icónicas del sleepy con papas')
async def sleepy_hall_of_fame(ctx):
    quotes = [
        'uhh que dificil está levantarse de la cama',
        'me voy a merendar y vuelvo',
        'que partida de mierda que estoy teniendo',
        'estoy on en twitch padre',
        'como cuesta levantarse chee',
        'que paja numerico boludo',
        'pero mama no ves que no estoy gritando',
        'na man sos un mogolico',
        'que buena que esta esa minusa',
        'que ganas de tener plata y ser fachero la puta madre',
        'voy a dejar esta materia de mierda'
    ]
    response = choice(quotes)
    await ctx.send(response)

@fran.command(name='animes', help='Te tiramo un anime random para que disfrutes de la vida, con algunas'
                                  'observaciones o consideraciones para que lo veas')
async def animes_que_tenes_que_ver(ctx):
    #No se como pingo se hace para poner solo una comilla xd
    quotes = [
        "Naruto y Naruto Shippuden (sin relleno miralo)",
        "Fullmetal Alchemist (el brotherhood es la misma hisotria)",
        "Death Note (para sleepyfran de los mejores animes de la historia)",
        "Haikyuu (si te gusta el voley)",
        "Evangelion (si entendes el final te mereces graduarte en harvard)",
        "Shingeki no kyojin (titanes contra humanos, epico)",
        "One punch man (realmente no tiene desperdicio y saitama es god)",
        "Avatar (no es un anime en si, pero no verlo es un pecado capital)"
        "Sword Art Online (es una simulacion en un anime, imaginate las posibilidades)"
    ]
    randanime = choice(quotes)
    await ctx.send(randanime)

fran.run(TOKEN)