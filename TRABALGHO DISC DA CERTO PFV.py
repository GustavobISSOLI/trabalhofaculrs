import discord
from discord import app_commands
import random
import pylance

id do servidor = 1124460501502525540

class client(discord.Client):
    def __init__ (self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

       
        async def on_ready(self):
            await self.wait_until_ready()
            if not self.synced:
                await tree.sync(guild= discord.Object(id=id_do_servidor))
                self.synced = true 
                print(f"E")
                print(f"Entramos como{self.user}")

aclient = client ()
tree = app_commands.CommandsTree(aclient)


@tree.commands(guild = discord.object(id=id_do_servidor), name="teste", description="Testando bot")
async def  testcmd(interaction: discord.Integration):
@tree.command(guilde= discord.Object(id=id_do_servidor), name = "dado", description = "Numero de um dado aleatório")
    
async def dado(interaction: discord.Integration):
    numero = random.randint (1,6)
    await interaction.response.send_message(f"Dado Número: {numero}", phemeral = False)
    aclient.run("MTEyNDEwODUzMjA3ODM0NjM0MQ.G_y38I.zzY4_0HHxkw3LGhFXhgiXjC0Mlju_I5zQRtGow")
