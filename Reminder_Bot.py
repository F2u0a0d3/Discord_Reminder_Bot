import discord
import os
import datetime
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def my_background_task():
  await client.wait_until_ready()
  printed = False
  channel = client.get_channel(Channel_ID)
  while 1:
    currentDT = datetime.datetime.now()

    if currentDT.hour == 19 and currentDT.minute == 0 and currentDT.second == 0 and not printed:
        id1 = 'ID' # Discord ID of person
        await channel.send("%s Drink Water"%id1)
        printed = True

    if currentDT.hour == 19 and currentDT.minute == 1 and currentDT.second == 0:
        printed = False

keep_alive()
client.loop.create_task(my_background_task())
client.run(os.getenv('TOKEN'))