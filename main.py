import discord
from discord.ext import commands
from discord.utils import get
import config
import asyncio

bot = commands.Bot(command_prefix = '/')
client = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message == bot.user:
        return
    if message.content.startswith('Hola'):
        await message.channel.send('Holaaa!')

@bot.command(pass_context = True)
async def conectar(ctx):
    canal = ctx.message.author.voice.channnel
    if not canal:
        await ctx.send('No estas conectado a un canal')
        return
    voz = get(bot.voice_clients,guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()

token = config.token
bot.run(token)
