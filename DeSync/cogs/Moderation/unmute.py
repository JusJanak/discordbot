#\\-MADE BY JANAK-//

import discord

from discord.ext import commands

class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

#\\-MADE BY JANAK-//
#Unmute Command
    @commands.has_permissions(manage_messages = True)
    @commands.command(aliases = ["Unmute"])
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name = "Muted")

        await member.remove_roles(mutedRole)
        
        embed = discord.Embed(
            title = f"{member.mention} was unmuted",
            description = f"{member.mention} was unmuted",
            color = 0x40ff00
        )

        await ctx.send(embed = embed)
        await member.send(f"You were unmuted in {guild.name}")
    
    @unmute.error
    async def unmute_error(self, ctx, error):
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
    client.add_cog(unmute(client))

#\\-MADE BY JANAK-//