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
    # SauceNao functionality
    if message.content.startswith("^source"):
        try:
            attachmentDict = message.attachments[0]
            sauce_list = revsearch.get_sauce_nao(attachmentDict["url"])
            if sauce_list["found"]:
                similarity = sauce_list["similarity"]
                thumbnail = sauce_list["thumbnail"]
                embed = discord.Embed(title="Saber Search",
                                      description=f"I'm {similarity}% sure it "
                                      "is this. Umu!", color=0xff0000)
                embed.set_image(url=thumbnail)
                embed.set_thumbnail(
                    url="https://padoru.moe/data/padoru.png")
                embed.add_field(name="Title", value=sauce_list["title"])
                embed.add_field(name="Artist", value=sauce_list["name"])
                embed.add_field(name="ID", value=sauce_list["id"])
                embed.add_field(name="URL", value=sauce_list["url"])
                await bot.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Saber Search",
                                      description="Khh-- I can't find it",
                                      color=0xff0000)
                embed.set_thumbnail(
                    url="https://padoru.moe/data/padoru.png")
                await bot.send_message(message.channel, embed=embed)
        except Exception as e:
            print(e)
            embed = discord.Embed(title="Saber Search",
                                  description="Guh I don't like that, "
                                  "did you even upload an image?",
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://padoru.moe/data/padoru.png")
            await bot.send_message(message.channel, embed=embed)


bot.run(DISCORD_TOKEN)
