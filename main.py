from lib2to3.pygram import Symbols
from tokenize import String
from discord.ext import commands
import discord
import asyncio
import math
import random

intents = discord.Intents.all()
lcase = "abcdefghijklmnopqrstuvwxyz"
ucase = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
n = "0123456789"
symbol = "[]{}#()*;._-"
ans = lcase + ucase + n + symbol
mpin = n
l = 9
lm = 4
password = "".join(random.sample(ans,l))
password1 = "".join(random.sample(mpin,lm))

client = commands.Bot(command_prefix='.', intents=intents)

@client.command()
async def echo(ctx: commands.Context, *msg):
    await ctx.reply(' '.join(msg))

@client.command()
async def add(ctx, num1 : float, num2 : float):
  answer = num1 + num2

  ans_em = discord.Embed(title = 'Addition', description = f'Question: {num1} + {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(13, 255, 251))
  await ctx.send(embed = ans_em)

@client.command()
async def sub(ctx, num1 : float, num2 : float):
  answer = num1 - num2

  ans_em = discord.Embed(title = 'Subtraction', description = f'Question: {num1} - {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(255, 13, 17))

  await ctx.send(embed = ans_em)


@client.command()
async def div(ctx, num1 : float, num2 : float):
  answer = num1 / num2

  ans_em = discord.Embed(title = 'Division', description = f'Question: {num1} / {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(252, 252, 0))
  
  await ctx.send(embed = ans_em)

@client.command()
async def mul(ctx, num1 : float, num2 : float):
  answer = num1 * num2

  ans_em = discord.Embed(title = 'Multiplication', description = f'Question: {num1} * {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(0, 255, 26))

  await ctx.send(embed = ans_em)

@client.command()
async def avg(ctx, num1 : float, num2 : float):
  answer = (num1 + num2)/2

  ans_embed = discord.Embed(title = 'Average', description = f'Question: Average of {num1} and {num2}\n\nAnswer: {answer}', colour = discord.Colour.blurple())

  await ctx.send(embed = ans_embed)

@client.command()
async def pow(ctx, num1 : float, num2 : float):
  answer = (num1 ** num2)

  ans_embed = discord.Embed(title = 'Power', description = f'Question: {num1} to the power of {num2}\n\nAnswer: {answer}', colour = discord.Colour.yellow())

  await ctx.send(embed = ans_embed)

@client.command()
async def sqrt(ctx, num1 : float):
  answer = math.sqrt(num1)

  ans_embed = discord.Embed(title = 'Square root', description = f'Question: Square root of {num1}\n\nAnswer: {answer}', colour = discord.Colour.dark_red())

  await ctx.send(embed = ans_embed)

@client.command()
async def cbrt(ctx, num1 : float):
  answer = (num1**(1/3))

  ans_embed = discord.Embed(title = 'Cube root', description = f'Question: Square root of {num1}\n\nAnswer: {answer}', colour = discord.Colour.brand_green())

  await ctx.send(embed = ans_embed)

@client.command()
async def dm(ctx, user: discord.Member, *,msg):
    embed = discord.Embed(title=msg,colour = discord.Colour.from_rgb(13, 255, 251))
    await user.send(embed=embed)

@client.command()
async def ping(ctx: commands.Context, *msg):
    await ctx.reply('pong! hehe')

@client.command()
async def gpass(ctx, user: discord.Member, *msg):
    embed = discord.Embed(title = 'Your genrated password is: ',description = {password} ,colour = discord.Colour.from_rgb(13, 255, 251))
    await user.send(embed=embed)

@client.command()
async def gmpin(ctx, user: discord.Member, *msg):
    embed = discord.Embed(title = 'Your genrated password is: ',description = {password1} ,colour = discord.Colour.from_rgb(13, 255, 251))
    await user.send(embed=embed)



client.run('') //enter your own client code here
