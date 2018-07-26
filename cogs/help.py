import asyncio
import discord
from discord.ext import commands

class Help:
    def __init__(self, bot):
       self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def help(self, ctx):
        embed = discord.Embed(title="General Help", description="https://lxstnlxv.github.io", color=0xFF6DEB)
        embed.add_field(name="How do I join a chat-room?", value="go onto connect-to-chat and upvote the corresponding emoji you would like to connect to")
        embed.add_field(name="How do I leave a chat-room?", value="go onto connect-to-chat and remove the corresponding emoji vote you would like to disconnect from")
        embed.add_field(name="Restrictions", value="You may only join one chat-room at a time, to join another chatroom you must remove your vote from all emojis possible then upvote the one you would like to connect to. If a room is full you may not join as you will be sent a message.")
        await self.bot.send_message(ctx.message.author, embed=embed)
    
    async def on_member_join(self, member):
        y = self.bot.get_server("471338151626145802")
        x = discord.utils.get(y.channels, name='global-chat')
        await self.bot.send_message(x, "{} has joined the server".format(member.name))
        await self.bot.send_message(member, "Welcome to MMS, a place to talk and have fun. This server is very straight forward but you may do >help if you need any help with this server.")

def setup(bot):
    bot.add_cog(Help(bot))