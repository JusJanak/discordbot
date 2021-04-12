#\\-MADE BY JANAK-//

import discord

from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

#\\-MADE BY JANAK-//
#Ban Command
    @commands.has_permissions(ban_members = True)
    @commands.command(aliases = ["Ban"])
    async def ban(self, ctx , member : discord.Member, *, reason = None):
        await ctx.member.ban(reason = reason)
        embed = discord.Embed(
            title = "Player was Banned.", 
            description = f"{member.mention} was banned from the server.", 
            color = 0x40ff00
        )
        await ctx.send(embed = embed)
    
    @ban.error
    async def ban_error(self, ctx, error):
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
                description = "The argument was not valid, Please try passing a valid argument. \n\nTry using '-Ban <User> <Reason>'",
                color = 0xff0000
            )
            await ctx.send(embed = embed)
        else:
            print(error)

#\\-MADE BY JANAK-//

def setup(client):
    client.add_cog(ban(client))

#\\-MADE BY JANAK-//
