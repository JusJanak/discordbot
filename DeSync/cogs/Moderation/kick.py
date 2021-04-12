#\\-MADE BY JANAK-//

import discord

from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, client):
        self.cleint = client

#\\-MADE BY JANAK-//
    #Kick Command
    @commands.has_permissions(kick_members = True)
    @commands.command(aliases = ["Kick"])
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await ctx.member.kick(reason = reason)
        embed = discord.Embed(
            title = "Player was kicked.", 
            description = f"{member.mention} was kicked out of the server.", 
            color = 0x40ff00
        )
        await ctx.send(embed = embed)
    
    @kick.error
    async def kick_clear(self, ctx, error):
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
                description = "The argument was not valid, Please try passing a valid argument. \n\nTry using '-Kick <User> <Reason>'",
                color = 0xff0000
            )
            await ctx.send(embed = embed)
        else:
            print(error)

        

def setup(client):
    client.add_cog(kick(client))

#\\-MADE BY JANAK-//