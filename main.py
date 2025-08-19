import random
import discord
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
  Player1_Health = 20
  Player2_Health = 20
  Atk = random.randint(1, 10)
  Atk2 = random.randint(1, 10)

  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello World!')

    if message.content.startswith('$start'):
      embed = discord.Embed(
          title="Battle Box",
          description="Floor 1",
          color=discord.Color.blue()
      )
      
      hp_display = f"{self.Player1_Health} / 20"
      embed.add_field(
        name=message.author.name, 
        value = "HP: " + hp_display + " ATK: " + str(self.Atk), 
        inline=False
      )
      embed.set_image(url=message.author.avatar.url)
      embed.add_field(
        name= "ThunderO6" ,
        value= f"HP: {self.Player2_Health}/20" + " ATK: " + str(self.Atk2), 
        inline=False
      )
      embed.set_footer(text="Footer text here")
      await message.channel.send(embed=embed)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN')) #Token

