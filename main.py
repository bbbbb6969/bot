import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is online")
@bot.command()    #傳送某網路圖片
async def 打我巴掌(ctx):
    await ctx.send('http://n.sinaimg.cn/sinacn/w572h290/20180124/144f-fyqwiqk3525608.jpg')
@bot.command()    #傳送某網路圖片
async def 早安(ctx):
    await ctx.send('https://truth.bahamut.com.tw/s01/202204/0e9a5503e5e827eee40da49963cba2bb.JPG')
bot.run('OTY3NzcxNjgyNjM2OTcyMDYy.YmVJnQ.J1vT_7KGTIxN1SeMC82KqmCP-Do')