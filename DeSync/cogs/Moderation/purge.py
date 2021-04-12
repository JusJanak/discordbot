#\\-MADE BY JANAK-//

import discord

from discord.ext import commands


class purge(commands.Cog):
    def __init__(self, client):
        self.client = client


#\\-MADE BY JANAK-//
    #Purge Command
    @commands.has_permissions(manage_messages = True)
    @commands.command(aliases = ["Purge", "Clear", "purge"])
    async def clear(self, ctx, amount : int = None):
        await ctx.channel.purge(limit = amount + 1)
        embed = discord.Embed(
            title = "Purging is Complete",
            discription = f"{ctx.author.mention} Purged {amount} messages.",
            color = 0x40ff00
        )
        await ctx.send(embed = embed)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permession.",
                description = f"{ctx.author.mention} You do not have permission for this command.", 
                color = 0xff0000
            )  
            await ctx.send(embed = embed)
        else:
            print(error)

def setup(client):
    client.add_cog(purge(client))

#\\-MADE BY JANAK-//