#\\-MADE BY JANAK-//

import discord

from discord.ext import commands

class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

#\\-MADE BY JANAK-//
    #Unban Command   
    @commands.has_permissions(ban_members = True)
    @commands.command(aliases = ["Unban"])
    async def unban(self, ctx, member : discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discrimintor = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discrimintor) == (member_name, member_discrimintor):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title = f"{user} was Banned.",
                    description = f"The {user} was successfully banned",
                    color = 0x40ff00
                )
                await ctx.send(embed = embed)
                return

#\\-MADE BY JANAK-//  

    @unban.error
    async def unban_error(self, ctx, error):
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
                description = "The argument was not valid, Please try passing a valid argument. \n\nTry using `-Unban <User>`",
                color = 0xff0000
            )
            await ctx.send(embed = embed)
        else:
            print(error)

#\\-MADE BY JANAK-//

def setup(client):
    client.add_cog(unban(client))
    