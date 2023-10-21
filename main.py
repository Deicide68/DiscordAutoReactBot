import discord
import data
 
# Bot here
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print ("Bot is ready")
 
@client.event
async def on_message(message):
    if(message.author.id == data.user_id):
        print(f"On message: {message.author.name}")
        await message.add_reaction(data.reaction)
 
client.run(data.bot_token)