import asyncio
import discord
from discord.ext import commands

lovechatroleids_1to4 = ["471374337828454412", "471374346565320710", "471374349119651840", "471374350688452661"]
lovechatroleids_5to8 = ["471374353532059659", "471374358208708618", "471374360276500480", "471374361887113227"]
lovechatroleids_9to10 = ["471374364277735424", "471374365930422282"]

class Roles:
    def __init__(self, bot):
       self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role('sysadmin')
    async def listrole(self, ctx):
        embed = discord.Embed(title="Chats 1-4", description="These are the public 10 person chat rooms", color=0xFF6DEB)
        msg1 = await self.bot.send_message(ctx.message.channel, embed=embed)
        await self.bot.add_reaction(msg1, "mms1:471488220933390337")
        await self.bot.add_reaction(msg1, "mms2:471488333856505856")
        await self.bot.add_reaction(msg1, "mms3:471491359178489876")
        await self.bot.add_reaction(msg1, "mms4:471491085714325524")
        embed = discord.Embed(title="Chats 5-8", description="These are the public 6 person chat rooms", color=0xFF6DEB)
        msg2 = await self.bot.send_message(ctx.message.channel, embed=embed)
        await self.bot.add_reaction(msg2, "mms5:471490824622964737")
        await self.bot.add_reaction(msg2, "mms6:471490516488421396")
        await self.bot.add_reaction(msg2, "mms7:471492010847633418")
        await self.bot.add_reaction(msg2, "mms8:471492277894774805")
        embed = discord.Embed(title="Chats 9-10", description="These are the public 2 person chat rooms", color=0xFF6DEB)
        msg3 = await self.bot.send_message(ctx.message.channel, embed=embed)
        await self.bot.add_reaction(msg3, "mms9:471492543465521154")
        await self.bot.add_reaction(msg3, "mms10:471493546944364544")

    async def check_if_full_and_join(self, idofrole, maxusers, user):
        x = 0
        y = self.bot.get_server("471338151626145802")
        for member in y.members:
            if idofrole in [role.id for role in member.roles]:
                x = x + 1
        if x >= maxusers:
            await self.bot.send_message(user, "Sorry there are too many people within this chatroom please wait...")
            return
        await self.bot.add_roles(user, discord.utils.get(y.roles, id=idofrole))

    async def on_reaction_add(self, reaction, user):
        roleChannelId = '471424029086187530'
        if "471370942665195546" in [role.id for role in user.roles]:
            return
        for x in lovechatroleids_1to4:
            if x in [role.id for role in user.roles]:
                return
        for x in lovechatroleids_5to8:
            if x in [role.id for role in user.roles]:
                return
        for x in lovechatroleids_9to10:
            if x in [role.id for role in user.roles]:
                return     
        if reaction.message.channel.id != roleChannelId:
            return
        if str(reaction.emoji) == "<:mms1:471488220933390337>":
            await self.check_if_full_and_join(lovechatroleids_1to4[0], 10, user)
        if str(reaction.emoji) == "<:mms2:471488333856505856>":
            await self.check_if_full_and_join(lovechatroleids_1to4[1], 10, user)
        if str(reaction.emoji) == "<:mms3:471491359178489876>":
            await self.check_if_full_and_join(lovechatroleids_1to4[2], 10, user)
        if str(reaction.emoji) == "<:mms4:471491085714325524>":
            await self.check_if_full_and_join(lovechatroleids_1to4[3], 10, user)    
        if str(reaction.emoji) == "<:mms5:471490824622964737>":
            await self.check_if_full_and_join(lovechatroleids_5to8[0], 6, user)
        if str(reaction.emoji) == "<:mms6:471490516488421396>":
            await self.check_if_full_and_join(lovechatroleids_5to8[1], 6, user)
        if str(reaction.emoji) == "<:mms7:471492010847633418>":
            await self.check_if_full_and_join(lovechatroleids_5to8[2], 6, user)
        if str(reaction.emoji) == "<:mms8:471492277894774805>":
            await self.check_if_full_and_join(lovechatroleids_5to8[3], 6, user)
        if str(reaction.emoji) == "<:mms9:471492543465521154>":
            await self.check_if_full_and_join(lovechatroleids_9to10[0], 2, user)
        if str(reaction.emoji) == "<:mms10:471493546944364544>":
            await self.check_if_full_and_join(lovechatroleids_9to10[1], 2, user)
            

    async def on_reaction_remove(self, reaction, user):
        roleChannelId = '471424029086187530'
        if reaction.message.channel.id != roleChannelId:
            return
        if str(reaction.emoji) == "<:mms1:471488220933390337>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-1'))
        if str(reaction.emoji) == "<:mms2:471488333856505856>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-2'))
        if str(reaction.emoji) == "<:mms3:471491359178489876>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-3'))
        if str(reaction.emoji) == "<:mms4:471491085714325524>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-4'))      
        if str(reaction.emoji) == "<:mms5:471490824622964737>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-5'))
        if str(reaction.emoji) == "<:mms6:471490516488421396>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-6'))
        if str(reaction.emoji) == "<:mms7:471492010847633418>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-7'))
        if str(reaction.emoji) == "<:mms8:471492277894774805>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-8'))
        if str(reaction.emoji) == "<:mms9:471492543465521154>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-9'))
        if str(reaction.emoji) == "<:mms10:471493546944364544>":
            await self.bot.remove_roles(user, discord.utils.get(reaction.message.server.roles, name='in-chat-10'))

def setup(bot):
    bot.add_cog(Roles(bot))