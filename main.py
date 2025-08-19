import discord
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
  Player1_Health = 20;
  Player2_Health = 20;

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
      embed.add_field(name=message.author.name ,value= self.Player1_Health, inline=False)
      embed.set_image(url=message.author.avatar.url)
      embed.add_field(name="HP", value=self.Player1_Health, inline=True)
      embed.add_field(name=message.author.name ,value= self.Player2_Health, inline=False)
      embed.add_field(name="Field 3", value="Another value", inline=True)
      #embed.set_thumbnail(url=message.author.avatar.url)     
      embed.set_footer(text="Footer text here")
      #embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
      await message.channel.send(embed=embed)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN')) #Token

