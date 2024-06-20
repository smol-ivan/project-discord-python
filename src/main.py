import os
import discord 
import requests
import json

# You can use the dotenv package to load the environment variables from a .env file, if you do not have a .env file this is not necessary, just replace SECRET_TOKEN with your discord token
from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__prefix_cmd = '&' 

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        # ignore messages from the bot itself
        if message.author == self.user: 
            return
        # The block of if statements below are the commands that the bot will respond to
        if message.content.startswith(f'{self.__prefix_cmd}hello'):
            await message.channel.send('Hello World from a bot!')

        if message.content.startswith(f'{self.__prefix_cmd}meme'):
            meme = await self.get_meme()
            await message.channel.send(meme)

    async def get_meme(self):
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        return json_data['url']

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(SECRET_TOKEN)