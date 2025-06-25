import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Keyword/response
keyword_responses = {
    "3": "https://tenor.com/view/say-that-again-gif-968943876633031890",
    "three": "https://tenor.com/view/say-that-again-gif-968943876633031890",
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg_lower = message.content.lower()
    for keyword, response in keyword_responses.items():
        if keyword in msg_lower:
            await message.reply(response)
            break

    await bot.process_commands(message)

bot.run("YOUR_BOT_TOKEN")