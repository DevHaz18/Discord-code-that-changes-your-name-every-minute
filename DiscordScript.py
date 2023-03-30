import discord
import asyncio
import random

# Replace with your Discord token
TOKEN = 'your_token_here'

client = discord.Client()

async def change_name():
    await client.wait_until_ready()
    while not client.is_closed():
        # Generate a random name
        new_name = 'Name ' + str(random.randint(1, 100))
        # Change the name
        await client.user.edit(username=new_name)
        # Wait for 1 minute
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print('Bot is ready.')

client.loop.create_task(change_name())
client.run(TOKEN)
