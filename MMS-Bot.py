import discord
from discord.ext import commands
import sys, traceback
import os


extension_list = ['cogs.admin', 'cogs.roles', 'cogs.help', 'cogs.test']

bot = commands.Bot(command_prefix='>', description="General Bot")
bot.remove_command('help')

if __name__ == '__main__':
    for extension in extension_list:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed nigga')
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in buddy')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name=">help"))

bot.run(os.environ['BOT_TOKEN'])
