import discord as ds
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice
        if not channel:
            await ctx.send('You need to be on a Voice Channel to be able to hear me bitch')
        await channel.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if not ctx.voice_client:
            await ctx.send('De donde me querés hechar amigue ¬.¬')
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Weno, ya no me quieren por aki')

    @commands.command(name='fumeteo', help='Fran te da una mano para llegar al cielo')
    async def fumeteo_time(self, ctx, url="https://www.youtube.com/watch?v=Wv0OrskppsY"):
        voice_channel = ctx.guild.voice_client
        player = await voice_channel.create_ytdl_player(url)
        player.start()

def setup(bot):
    bot.add_cog(Music(bot))