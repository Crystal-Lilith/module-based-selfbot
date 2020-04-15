from discord import Client

from asyncio import sleep
from random import randint

import config

from importlib import import_module # Using importlib's `import_module` function is preferred over Python's built-in `__import__`

bot = Client()


commands = {}
for file in import_module('os').listdir(import_module('os').path.join('.', 'cmds')):
    cmd = import_module("cmds."+file)
    # The following code is going to check if the command is valid, if it is, then register it
    if not isinstance(cmd.aliases, list):
        print("Command alias is not a list, skipping "+file)
    if not isinstance(cmd.aliases, str):
        print("Command alias is not a string, skipping "+file)
    for alias in cmd.aliases:
        commands[alias] = {"code":cmd.code, "alias":True, "original_name":cmd.name}
    commands[cmd.name] = {"code":cmd.code, "alias":False, "original_name":cmd.name}


enabled_channels = []

class temp:

    async def embed(msg, args):
        try:
            if args[0] == '':
                args[0] = None
            if args[1] == '':
                args[1] = None
            hex=eval(args[2])
        except IndexError:
            hex=randint(0,16777215)
        try:
            await msg.channel.send(embed=discord.Embed(title=args[1], description=args[0], colour=hex))
        except IndexError:
            try:
                await msg.channel.send(embed=discord.Embed(description=args[0], colour=hex))
            except IndexError:
                await msg.channel.send(embed=discord.Embed(colour=hex))

@bot.event
async def on_message(msg):
    if msg.author.id == bot.user.id and msg.content == '/enable_channel' and msg.channel not in enabled_channels:
            enabled_channels.append(msg.channel)
            print("Channel added to enabled channels list")
    elif msg.author.id not in config.allowed_ids+[bot.user.id] and msg.content == '/disable_channel' and msg.channel in enabled_channels:
        enabled_channels.pop(enabled_channels.index(msg.channel))
    if msg.author.id not in bot.user.id:
        if config.enabled_by_default != True:
            return
    try:
        for cmd in commands:
            if msg.content.startswith(config.prefix+cmd):
                msg.args = msg.content[len(config.prefix+cmd+" "):].split(config.splitter)
                await commands[cmd](msg)
            else:
                return
    except KeyError:
        pass

bot.run(config.token, bot=False)
