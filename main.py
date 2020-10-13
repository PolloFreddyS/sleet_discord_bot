import os
from discord.ext import commands
from discord.ext.commands import has_permissions
bot_token = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command()
@has_permissions(administrator=True)
async def muteall(ctx):
    channel_requested = ctx.author.voice.channel
    all_channel_members = ctx.channel.members
    for i in range(len(all_channel_members)):
        if not all_channel_members[i].bot:
            if all_channel_members[i].voice is not None:
                if all_channel_members[i].voice.channel == channel_requested:
                    await all_channel_members[i].edit(mute=True)


@bot.command()
@has_permissions(administrator=True)
async def unmuteall(ctx):
    channel_requested = ctx.author.voice.channel
    all_channel_members = ctx.channel.members
    for i in range(len(all_channel_members)):
        if not all_channel_members[i].bot:
            if all_channel_members[i].voice is not None:
                if all_channel_members[i].voice.channel == channel_requested:
                    await all_channel_members[i].edit(mute=False)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(bot_token)
