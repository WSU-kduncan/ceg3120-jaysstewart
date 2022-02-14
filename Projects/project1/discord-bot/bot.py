import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

   # voice lines from video game Escape from Tarkov

   # scav voicelines
    scav = [
        'Cheeki Breeki bansku hiki!',
        'Von on Cyka!',
        'Opachki',
        'Kepka'
    ]

    # usec voicelines
    usec = [
        'Goddamn ruskies',
        'Damn Ivans',
        'Okay we got BEARS, now we have god damn scavs',
        'Just die already!',
        'Fuckin scav',
        'I hear a rat'
    ]

    if message.content == 'scav!':
        response = random.choice(scav)
        await message.channel.send(response)
    elif message.content == 'usec!':
        response = random.choice(usec)
        await message.channel.send(response)
    elif message.content == 'onion!':
       # picture of spider man enjoying a delicous onion ring
        response = 'https://i.redd.it/4g4r7ks7f0531.jpg'
        await message.channel.send(response)

client.run(TOKEN)
