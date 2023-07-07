import discord
from discord import app_commands
from discord.ext import commands
import json
import os
import asyncio

tocken = 'MTExOTk1MDk4NTQ4MjIxMTM1MA.GujVo0.9Mqw_6SbNELkj4cBE_5u_LNmBmwok_FvSLDxxM'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='b!', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
  print("I am Online!")
  activity = discord.Game(name="Type gas!help ", type=3)
  await bot.change_presence(activity=activity)
  try:
    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} Commands')

    data = {'synced': len(synced)}

    with open('database.json', 'w') as f:
      json.dump(data, f)
  except Exception as e:
    print(e)


@bot.tree.command(name='help', description='Shows Help Message.')
async def help(interaction: discord.Interaction):
  embed = discord.Embed(color=0xe942f5)
  embed.add_field(name='**This Is The Help Menue!**',
                  value="Prefix: `b! & (/)` \n **Commands(2)**")
  embed.set_author(name=interaction.user.name,
                   icon_url=interaction.user.avatar)

  await interaction.response.send_message(embed=embed)

@bot.tree.command(name='setup')

bot.run(tocken)
