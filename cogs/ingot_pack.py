import os, discord, requests, random, urllib.request
from discord.ext import commands
from PIL import Image

backing_image_path = "assets/display/backing.png"
temporary_image_path = "assets/temporary/temporary.png"
random_ingots_path = "assets/display/random_ingots/"

class IngotPackCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Search for an ingot or ingotmoji")
    async def search(
        self,
        ctx,
        mode: discord.Option(str, choices=["item", "emoji"]),
        name: discord.Option(str),
        raw:  discord.Option(bool, required=False, default=False)
        ):

        ingot_name = str(name).lower().replace("_", " ")
        ingot_file_name = str(name).lower().replace(" ", "_")

        if ingot_name == "hello" or ingot_name == "turtle" or ingot_name == "vedal":
            embed = discord.Embed(color=discord.Colour.green())
            embed_file = discord.File("assets/display/vedal.gif")
            embed.set_image(url="attachment://vedal.gif")
            await ctx.respond(embed=embed, file=embed_file)
            return

        if mode == "item":
            ingot_url = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/minecraft/textures/item/" + ingot_file_name + ".png"
        else:
            ingot_url = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/emoji/" + ingot_file_name + ".png"

        try:
            urllib.request.urlretrieve(ingot_url, temporary_image_path)
        except Exception as error:
            if "404" in str(error):
                await ctx.respond("Sorry, that ingot doesn't seem to exist. Are you sure you spelled it correctly?", ephemeral=True)
            else:
                await ctx.respond("Uh oh, there's been some kind of error. Please try again.", ephemeral=True)
                print(error)
            return

        # ingo descripto
        ingot_description = requests.get('https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/ing-bot/descriptions/' + ingot_file_name + '.txt').content.decode('utf-8')

        # dumb rendering time!!!!
        if mode == "emoji":
            if not raw:
                ingot_image = Image.open(temporary_image_path)
                ingot_image = ingot_image.resize((256, 256), 0)
                ingot_image.save(temporary_image_path)
        elif not raw:
            base_image = Image.open(backing_image_path).convert("RGBA")
            ingot_image = Image.open(temporary_image_path).convert("RGBA")

            random_ingots = []
            for i in range(8):
                random_ingot_path = random_ingots_path + random.choice(os.listdir(random_ingots_path))
                random_ingots.append(Image.open(random_ingot_path).convert("RGBA"))

            base_image.paste(ingot_image, (6, 6), ingot_image)
    
            random_ingot_positions = [(-12, -12), (6, -12), (24, -12), (-12, 6), (24, 6), (-12, 24), (6, 24), (24, 24)]
            for i in range(8):
                base_image.paste(random_ingots[i], random_ingot_positions[i], random_ingots[i])

            base_image = base_image.resize((504, 504), 0)
            base_image.save(temporary_image_path)

        embed = discord.Embed(title=ingot_name.title(), color=discord.Colour.blurple(), url=ingot_url)
        if ingot_description != '404: Not Found':
            embed.description = ingot_description
        embed_file = discord.File(temporary_image_path, filename="ingot.png")
        embed.set_image(url="attachment://ingot.png")

        await ctx.respond(embed=embed, file=embed_file)
        image = Image.new(mode="RGBA", size=(16, 16))
        image.save(temporary_image_path)

def setup(bot):
    bot.add_cog(IngotPackCommands(bot))