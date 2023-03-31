import os
import discord
import openai
from discord.ext import commands
import ssl

# Authenticate the bot using the bot token provided by Discord
intents = discord.Intents.default()  # Create a default intents object
intents.members = True  # Enable the members intent

bot = commands.Bot(command_prefix='!', intents=intents)  # Pass the intents object to the Bot constructor
bot_token = os.environ['BOT_TOKEN'] = 'MTA3NzIwNTA4NDM5NzYzNzc5Mg.GGeAu8.Yfrm_B3R7z1niKGtxkNLWeKB_MDfsfNZcAjVMA'
openai.api_key = os.environ['openai.api_key '] = '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'
# ID of the channel that the bot will focus on
channel_id = '1091276125235327036'

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE


# Connect to the Discord server
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Receive messages from the Discord server and send them to the ChatGPT model
@bot.event
async def on_message(message):
    if message.channel.id != channel_id:
        return

    if message.author == bot.user:
        return

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=message.content,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Send the response from the ChatGPT model back to the Discord server
    await message.channel.send(response.choices[0].text)

# Run the bot
bot.run(bot_token)
