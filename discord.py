import discord
from discord import app_commands
import random

id_do_servidor = 1124460501502525540

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True
            print(f"Entramos como {self.user}")

client = Client()
tree = app_commands.CommandsTree(client)


@tree.commands(guild=discord.Object(id=id_do_servidor), name="teste", description="Testando bot")
async def testcmd(interaction: discord.Interaction):
    await interaction.response.send_message("Teste de comando", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor), name="dado", description="Número de um dado aleatório")
async def dado(interaction: discord.Interaction):
    numero = random.randint(1, 6)
    await interaction.response.send_message(f"Dado Número: {numero}", ephemeral=False)


client.run("MTEyNDEwODUzMjA3ODM0NjM0MQ.G_y38I.zzY4_0HHxkw3LGhFXhgiXjC0Mlju_I5zQRtGow")
