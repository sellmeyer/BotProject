import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

'#Ready Check'
@client.event
async def on_ready():
    print('Ready')


@client.event
async def on_member_join(member):
    print(f'{member} A member has joined') 


@client.event
async def on_member_remove(member):
    print(f'{member} A member has left')     


@client.command()
async def ping(ctx):
    await ctx.send(f'ping is {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['8Ball responses'
    ]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=None)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=None)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

'# load'
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

"# unload"
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('DiscordTokenGoesHere')