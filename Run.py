import yaml
import sys
import os

from util.config import create_config
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
create_config()

with open("cfg/config.yml", 'r') as f:

    config_cfg = yaml.safe_load(f)

with open("cfg/cogs.yml", 'r') as f:

    cog_cfg = yaml.safe_load(f)

# Add cogs from cogs.yml file
initial_extensions = []
for c in cog_cfg:

    if cog_cfg[c]:

        initial_extensions.append(c)

client = Bot(command_prefix=config_cfg['Prefix'])

# loading extensions/cogs for commands
if __name__ == '__main__':

    for extension in initial_extensions:

        client.load_extension(extension)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

client.run(os.getenv('DISCORD_TOKEN'))
