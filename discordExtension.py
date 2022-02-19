from discord.ext import commands, tasks
import threading
from findPracticals import *
import asyncio
from random import randint
from pass_from_config import get_cred, get_token

bot = commands.Bot(command_prefix='$')
dict = {'W': 'None', 'A': 'None', 'T': '', 'F': ''}
switch = True
pwd = ''
token = get_token()

@bot.command()
async def ping(ctx):
    await ctx.send('```Pong!```')


@bot.command()
async def start(ctx, args=''):
    global switch, pwd, username
    switch = True
    client = requests.Session()
    login(client, pwd, username)
    while switch:
        this_r = randint(30, 60)
        flag = main_scanner(client, dict, filter=args)
        if flag:
            await ctx.send(
                '```' + dict['F'] + '\nWoodlands: ' + dict['W'] + '\nAng Mo Kio: ' + dict['A'] + '\nRecorded on ' +
                dict[
                    'T'] + f'\n\nNext scan in {this_r} mins\nat {datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp() + (60 * this_r)).strftime("%d %b %y, %I:%M%p")}\n' + '```')
        if not switch:
            break
        await asyncio.sleep(60 * this_r)


@bot.command()
async def stop(ctx):
    global switch
    switch = False
    await ctx.send('Stopped monitoring process!')


async def default_check():
    global pwd, username
    await bot.wait_until_ready()
    channel = bot.get_channel(869133877401235486)
    await channel.send('Bot is online!')
    client = requests.Session()
    login(client, pwd, username)
    while switch:
        this_r = randint(30, 60)
        flag = main_scanner(client, dict, filter=args)
        if flag:
            await channel.send(
                '```' + dict['F'] + '\nWoodlands: ' + dict['W'] + '\nAng Mo Kio: ' + dict['A'] + '\nRecorded on ' +
                dict[
                    'T'] + f'\n\nNext scan in {this_r} mins\nat {datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp() + (60 * this_r)).strftime("%d %b %y, %I:%M%p")}\n' + '```')
        if not switch:
            break
        await asyncio.sleep(60 * this_r)


if __name__ == '__main__':
    username, pwd = get_cred()
    bot.loop.create_task(default_check())
    bot.run(token)
