import hikari
import lightbulb
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot = lightbulb.BotApp(
    token=os.environ.get("API_TOKEN"),
    default_enabled_guilds=(1047002328684838982)
)

@bot.command
@lightbulb.option('num', 'how many to add', type=int)
@lightbulb.command('add', 'add punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
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
    await context.respond(f'changed nickname to {prev_name} [{result}]')

@bot.command
@lightbulb.option('num', 'how many to remove', type=int)
@lightbulb.command('remove', 'remove punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    prev = context.member.nickname
    if '[' in prev and ']' in prev:
        prev_name = prev.split('[')[0][0:-1]
        prev_num = int(prev.split('[')[1][0:-1])
    else:
        prev_name = prev
        prev_num = 0
    result = int(prev_num) - context.options.num
    await context.member.edit(nickname = f"{prev_name} [{result}]")
    await context.respond(f'changed nickname to {prev_name} [{result}]')

bot.run()
