import os
import asyncio
from bot_functions import server_management
from discord.ext import commands
from discord.ext.commands import has_permissions
bot_token = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command()
@has_permissions(administrator=True)
async def muteall(ctx):
    mute_list = server_management.mute_members(ctx)
    for mute_member in mute_list:
        await mute_member


@bot.command()
@has_permissions(administrator=True)
async def unmuteall(ctx):
    mute_list = server_management.unmute_members(ctx)
    for mute_member in mute_list:
        await mute_member


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(bot_token)
