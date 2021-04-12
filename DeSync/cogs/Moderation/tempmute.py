import discord

from discord.ext import commands



class tempmute(commands.Cog):
    def __init__(self, client):
        self.client = client

 #TempMute Command   
    @commands.has_permissions(manage_messages = True)
    @commands.command(name = "Tempmute", aliases = ["tempmute"])
    async def mute_members(self, ctx, targets : discord.Member, hours: int, *, reason : str = "No Reason Provided."):

        if not len(targets):

            embed = discord.Embed(
                title = "Missing Required Arguments",
                description = f"{ctx.author.mention} One or more required arguments are missing.",
                color = 0xff0000
            )

            await ctx.send(embed = embed)
        else:
            unmutes = []
            
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name = "Muted")

            for target in targets:
                pass



def setup(client):
    client.add_cog(tempmute(client))