import discord
from discord.ext import commands
import revsearch
from config import DISCORD_TOKEN
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print("%s is now online" % bot.user.name)


@bot.event
async def on_message(message):
    print(message.content)
    if message.content.startswith("^source"):
        try:
            attachmentDict = message.attachments[0]
            sauce_list = revsearch.get_sauce_nao(attachmentDict["url"])
            if sauce_list["found"]:
                similarity = sauce_list["similarity"]
                thumbnail = sauce_list["thumbnail"]
                embed = discord.Embed(title="Sagiri Search", color=0x00ff00)
                embed.set_image(url=thumbnail)
                embed.set_thumbnail(
                    url="https://padoru.moe/data/padoru.png")
                embed.add_field(name="Title", value=sauce_list["title"])
                embed.add_field(name="Artist", value=sauce_list["name"])
                embed.add_field(name="ID", value=sauce_list["id"])
                embed.add_field(name="URL", value=sauce_list["url"])
                await bot.send_message(message.channel,
                                       content=f"I'm {similarity}% sure it's:",
                                       embed=embed)
            else:
                await bot.send_message(message.channel, ":/ couldn't find it")
        except Exception:
            await bot.send_message(message.channel,
                                   "I'm shittily coded atm, maybe you forgot "
                                   + "to attach a file, maybe I reached my "
                                   + "api limit, who knows")


@bot.command()
async def source(message):
    await bot.say(message.content)

bot.run(DISCORD_TOKEN)
