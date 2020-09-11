import discord
from discord.ext import commands
from discord.utils import get
import config
import asyncio

bot = commands.Bot(command_prefix = '!')
# client = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return

    if message.content.startswith('Hola'):
        await message.channel.send('Holaaa!')
    if message.content.startswith('Hello'):
        await message.channel.send('Helooo!')

@bot.command(pass_context = True)
async def connect(ctx):
    canal = ctx.message.author.voice.channnel
    if not canal:
        await ctx.send('You are not connected to any channel')
        return
    voz = get(bot.voice_clients,guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()

token = config.token
bot.run(token)
