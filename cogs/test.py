import asyncio
import discord
from discord.ext import commands

class Test:
    def __init__(self, bot):
       self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('sysadmin')
    async def listtermsofservices(self, ctx):
        embed = discord.Embed(title="Terms and Services", description="You must agree to these terms and services to be a part of thiserver:", color=0xFF6DEB)
        embed.add_field(name="Rule 1", value=":x: Do not make others feel too uncomfortable on purpose. :x:")
        embed.add_field(name="Rule 2", value=":book: You must be competent enough to be able to read carefully and listen to simple directions. :book:")
        embed.add_field(name="Rule 3", value=":thumbsup: You must be able to upvote emojis to obtain roles and access to chatrooms, so upvote the monkey. :thumbsdown:")
        msg1 = await self.bot.send_message(ctx.message.channel, embed=embed)
        await self.bot.add_reaction(msg1, "🦊")
        await self.bot.add_reaction(msg1, ":thinkingblackguy:472549593331138560")
    
    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('sysadmin')
    async def serverreset(self, idofrole, maxusers, user):
        y = self.bot.get_server("471338151626145802")
        for member in y.members:
            role = discord.utils.get(member.server.roles, name="Awaiting")
            await self.bot.add_roles(member, role)
    
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name="Awaiting")
        await self.bot.add_roles(member, role)

    async def on_reaction_add(self, reaction, user):
        roleChannelId = "472555998943510538"
        if reaction.message.channel.id != roleChannelId:
            return
        if str(reaction.emoji) == "<:thinkingblackguy:472549593331138560>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='Awaiting'))
            role = discord.utils.get(user.server.roles, name="Member")
            await self.bot.add_roles(user, role)
        else:
            await self.bot.send_message(user, "You did not upvote the monkey you retard.")
            await self.bot.kick(user)

def setup(bot):
    bot.add_cog(Test(bot))