import asyncio
import discord
from discord.ext import commands

class Admin:
    def __init__(self, bot):
       self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('mod')
    async def killclear(self, ctx, amount_of_messages: int):
        mgs = []
        number = int(amount_of_messages) + 1
        async for x in self.bot.logs_from(ctx.message.channel, limit=number):
            mgs.append(x)
        await self.bot.delete_messages(mgs)

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('mod')
    async def ban(self, ctx, member: discord.Member, reason):
        await self.bot.send_message(member, "You have been banned {} ".format(reason))
        await self.bot.ban(member)
        await self.bot.send_message(ctx.message.channel, "{} has been banned for {} ".format(member.name, reason))

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('mod')
    async def kick(self, ctx, member: discord.Member, reason):
        await self.bot.send_message(member, "You have been kicked for {} ".format(reason))
        await self.bot.kick(member)
        await self.bot.send_message(ctx.message.channel, "{} has been kicked for {} ".format(member.name, reason))

def setup(bot):
    bot.add_cog(Admin(bot))
