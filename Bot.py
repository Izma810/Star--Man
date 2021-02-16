import discord
import os
import asyncio
import random 
from discord.ext import commands

client=commands.Bot(command_prefix="^")
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game("Playing with the dead"))
  print("Ready :)")

@client.command()
async def avatar(ctx, *, member: discord.Member=None): 
    if not member: 
        member = ctx.message.author 
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)
@client.command()
async def ping(ctx):
  await ctx.send(f"Your ping:{round(client.latency*1000)}ms")
@client.command(aliases=["ques","test"])
async def _ques(ctx,*,question):
  responses=("It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
            "You bot stop asking me questions, tera naukar nahi hu")
  await ctx.send(f"Question:{question}\nAnswer:{random.choice(responses)}")
@client.command(pass_context=True)
async def help(ctx):
  author=ctx.message.author
  embed=discord.Embed(
    color=discord.Color.purple()

  )
  embed.set_author(name="Help")
  embed.add_field(name="^ping", value="Returns Pong!", inline=False)
  embed.add_field(name="^ques", value="Ask ques and get answers",inline=False)
  embed.add_field(name="^avatar", value="Displays avatar of the user",inline=False)
  embed.add_field(name="^whois", value="Shows username and ID",inline=False)
  embed.add_field(name="^meme", value="Displays fresh/rotten memes", inline=False)

  await ctx.send(author,embed=embed)
@client.command(aliases=["user","info"])
async def whois(ctx,member: discord.Member):
  embed=discord.Embed(title=member.name, description=member.mention, color=discord.Color.green())
  embed.add_field(name="ID", value=member.id, inline=True)
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by{ctx.author.name}")
  await ctx.send(embed = embed)
images=[
  "https://i.redd.it/2v3rwsofr1g61.png",
  "https://i.redd.it/tf4v7ns9u0g61.png",
  "https://i.redd.it/piytrz3zl1g61.jpg",
  "https://i.redd.it/t6wqevwtjzf61.jpg",
  "https://i.redd.it/5chmd0t3y0g61.png",
  "https://i.redd.it/hqgntbm6a1g61.png",
  "https://i.redd.it/pc25scls71g61.jpg",
  "https://i.redd.it/ml2nuryno0g61.jpg",
  "https://i.redd.it/nddvril770g61.png",
  "https://i.redd.it/uf7sv7t101g61.jpg",
  "https://i.redd.it/s8rkpjpgv0g61.jpg",
  "https://i.redd.it/x2jm23uy40g61.jpg",
  "https://i.redd.it/73njimobv0g61.jpg",
  "https://i.redd.it/9hqafjmfvzf61.jpg"
]
@client.command()
async def meme(ctx):
  embed=discord.Embed(color=discord.Color.red())
  random_link=random.choice(images)
  embed.set_image(url=random_link)
  await ctx.send(embed=embed)
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f"{amount} messages cleared")

  
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member,*,reason="No reason provided"):
  await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,*,reason="No reason provided"):
  await member.ban(reason=reason)



def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + "-" +json_data[0]["a"]
  return(quote)


tired_words=["I would like to take some rest now","I am tired now"]
working_words=["Ooooh make me a pro bot you fool, and btw you are still left with hindi work so keep working!!!","A great bot once said 'Never give up'"]
@client.command()
async def inspire(ctx):
  quote=get_quote()
  await ctx.send(quote)
@client.event
async def on_message(message):
  if any(word in message.content for word in tired_words):
    await message.channel.send(random.choice(working_words))

token=os.getenv("Discord_Bot_Token")
