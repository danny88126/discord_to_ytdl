import discord
from discord.ext import commands
from core.classes import Cog_Extension

class System(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    
    @commands.command()
    async def version(self, ctx):
        await ctx.send("v0.5")

def setup(bot):
    bot.add_cog(System(bot))