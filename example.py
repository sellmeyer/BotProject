import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot online, cogs loaded')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('cogPing')    


def setup(client):
    client.add_cog(Example(client))
