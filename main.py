import discord
import openai
from dotenv import load_dotenv
import os 
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")
ID_CHANNEL = os.getenv("CHANNEL_ID")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

openai.api_key=OPENAI_TOKEN

async def buscar_historico_canal(canal, limit=1):
    messages = []
    async for message in canal.history(limit=limit):
        messages.append(
            {
                "role":"user" if message.author.id!=bot.user.id else "system",
                "content":message.content,
            }
        )
    messages.reverse()
    return messages

def ask_gpt(messagens):
    response = openai.ChatCompletion.create(
        messages=messagens,
        model="gpt-3.5-turbo-16k",
        temperature=0.9,
        max_tokens=500,
    )
    
    return response.choices[0].message.content
    
@bot.event
async def on_ready():
    print(f"O {bot.user.name} está ativo!")

@bot.event
async def on_message(message):
    if message.author.bot or message.channel.id != CHANNEL_ID:
        return
    
    async with message.channel.typing():
        mensagens = await buscar_historico_canal(message.channel)
        resposta = ask_gpt(mensagens)
        
        await message.reply(resposta)
    
    await bot.process_commands(message)
    
    
bot.run(BOT_TOKEN)