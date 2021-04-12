import discord

from discord.ext import commands

client = commands.Bot(command_prefix = "-")

initial_extensions = [#
    #Moderation Cogs
    "cogs.Moderation.purge",
    "cogs.Moderation.kick",
    "cogs.Moderation.ban",
    "cogs.Moderation.unban",
    "cogs.Moderation.mute",
    "cogs.Moderation.unmute",
    "cogs.Moderation.tempmute",
]


if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is now Online...")



client.run("bot token")
