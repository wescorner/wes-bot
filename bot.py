import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='MTA0NzAwMTM2NzcyNzgzNzIxNA.GzlOiT.J7kinC5M1JQ1weuMYOflaJrXAmfqbfOPP2mGVo',
    default_enabled_guilds=(1047002328684838982)
)

@bot.command
@lightbulb.option('num', 'how many to add', type=int)
@lightbulb.command('add', 'add punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    prev = context.member.nickname
    result = int(prev) + context.options.num
    await context.member.edit(nickname = result)
    # await context.respond(prev)
    await context.respond(f'changed nickname to  {str(result)}')

@bot.command
@lightbulb.option('num', 'how many to remove', type=int)
@lightbulb.command('remove', 'remove punishment number')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    prev = context.member.nickname
    result = int(prev) - context.options.num
    await context.member.edit(nickname = result)
    await context.respond(f'changed nickname to  {str(result)}')

bot.run()