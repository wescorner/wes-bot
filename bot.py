import hikari
import lightbulb
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot = lightbulb.BotApp(
    token=os.environ.get("API_TOKEN"),
    default_enabled_guilds=(1047002328684838982, 984973732470751273)
)

@bot.command
@lightbulb.option('num', 'how many to add', type=int)
@lightbulb.command('add', 'add punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):
    prev = context.member.nickname
    print(context.member)
    if '[' in prev and ']' in prev:
        prev_name = prev.split('[')[0][0:-1]
        prev_num = int(prev.split('[')[1][0:-1])
    else:
        prev_name = prev
        prev_num = 0
    result = int(prev_num) + context.options.num
    await context.member.edit(nickname = f"{prev_name} [{result}]")
    await context.respond(f'{context.user.mention} added {context.options.num} to the counter.')

@bot.command
@lightbulb.option('num', 'how many to remove', type=int)
@lightbulb.command('remove', 'remove punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def remove(context):
    prev = context.member.nickname
    if '[' in prev and ']' in prev:
        prev_name = prev.split('[')[0][0:-1]
        prev_num = int(prev.split('[')[1][0:-1])
    else:
        prev_name = prev
        prev_num = 0
    result = int(prev_num) - context.options.num
    await context.member.edit(nickname = f"{prev_name} [{result}]")
    await context.respond(f'{context.user.mention} removed {context.options.num} from the counter.')

@bot.command
@lightbulb.command("league", "depression time")
@lightbulb.implements(lightbulb.SlashCommand)
async def league(context):
    await context.respond(context.user.mention)

bot.run()
