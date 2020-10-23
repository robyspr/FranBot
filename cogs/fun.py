import discord as ds
from random import choice
from discord.ext import commands

class FunTimes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot online')

    #Commands
    @commands.command(help='Tiro los mejores pls memes de la historia papA')
    async def memes(self, ctx):
        quotes = [
            'pls ohno sleepyfran',
            'pls whodidthis chowfran',
            'pls stroke hi',
            'pls boo , hola batman'
        ]
        response = choice(quotes)
        await ctx.send(response)

    @commands.command(aliases=['sleepyfran', 'sleepy'], help='Salen esas frases icónicas del sleepy')
    async def sleepy_hall_of_fame(self, ctx):
        quotes = [
            'uhh que dificil está levantarse de la cama',
            'me voy a merendar y vuelvo * nunca vuelve *',
            'que partida de mierda que estoy teniendo',
            'como cuesta levantarse chee'
        ]
        response = choice(quotes)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(FunTimes(bot))