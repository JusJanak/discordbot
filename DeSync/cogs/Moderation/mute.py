#\\-MADE BY JANAK-//

import discord

from discord.ext import commands

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

#\\-MADE BY JANAK-//
#Mute Command  
    @commands.has_permissions(manage_messages = True)
    @commands.command(aliases = ["Mute"])
    async def mute(self, ctx, member : discord.Member, *, reason = None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name = "Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak = False, send_messages = False,)

        await member.add_roles(mutedRole, reason = reason)
        embed = discord.Embed(
            title = f"{member.mention} was Muted.", 
            description = f"{member.mention} was muted for {reason}", 
            color = 0x40ff00
        )
        await ctx.send(embed = embed)
        await member.send(f"You were muted in {guild.name} for {reason}")
    
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permession.",
                description = f"{ctx.author.mention} You do not have permission for this command.", 
                color = 0xff0000
            )  
            await ctx.send(embed = embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "Argument not valid",
                description = "The argument was not valid, Please try passing a valid argument. \n\nTry using `-Mute <User> <Reason>`",
                color = 0xff0000
            )
            await ctx.send(embed = embed)
        else:
            print(error)

#\\-MADE BY JANAK-//

def setup(client):
    client.add_cog(mute(client))

#\\-MADE BY JANAK-//