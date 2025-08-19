from email import message
import random
import discord
import os
import asyncio
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
      Player1Hp = self.Player1_Health
      Player2Hp = self.Player2_Health
      atk1 = self.Atk
      atk2 = self.Atk2
      while Player1Hp > 0 and Player2Hp > 0:
        embed = discord.Embed(
          title="Battle Box",
          description="Floor 1",
          color=discord.Color.blue()
        )
        embed.add_field(
          name=message.author.name, 
          value = "HP: " + f"{Player1Hp}/20" + " ATK: " + f"{atk1}", 
          inline=False
        )
        embed.set_image(url=message.author.avatar.url)
        embed.add_field(
          name= "ThunderO6" ,
          value= f"HP: {Player2Hp}/20" + " ATK: " + f"{atk2}", 
          inline=False
        )
        Player1Hp -= atk2
        Player2Hp -= atk1
        Battle = (
          f"{message.author.name} attacks ThunderO6 for {atk1} damage!\n"
          f"ThunderO6 attacks {message.author.name} for {atk2} damage!\n"
        )
        embed.add_field(name="Battle Log", value=Battle, inline=False)
        await message.channel.send(embed=embed)
        await asyncio.sleep(3)

        if Player1Hp > 0 and Player2Hp <= 0:
          await message.channel.send(f"{message.author.mention} wins!")
          break
        elif Player2Hp > 0 and Player1Hp <= 0:
          await message.channel.send("ThunderO6 wins!")
          break
        elif Player1Hp <= 0 and Player2Hp <= 0:
          await message.channel.send("It's a draw!")
          break

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN')) #Token

