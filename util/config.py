import os
import sys
import yaml

def get_config():
    """ return the config dict object """

    if os.path.exists("cfg/config.yml"):

        with open("cfg/config.yml", 'r') as f:

            return yaml.safe_load(f)
    else:

        print("config.yml not found!")

def create_config():
    """ Check to see if config file has been created and if not then create one! """

    if not os.path.exists("cfg"): os.mkdir("cfg")

    if not os.path.exists("cfg/config.yml"):

        cfg = {
            "Staff_Roles": ["Scrim-Organizer", "Moderator"],
            "Prefix": ["!! ", "!!"],
            "Allowed_Channels": [0, 0]
        }

        with open("cfg/config.yml", 'w') as f:
            
            yaml.safe_dump(cfg, f)

        print("Created config in 'cfg/config.yml'")

        __create_cogs_config()

        sys.exit(0)

def __create_cogs_config():
    """ Check to see if cogs.yml file has been created """

    if not os.path.exists("cfg/cogs.yml"):

        cfg = {
            "cogs.queue": True
        }

        with open("cfg/cogs.yml", 'w') as f:

            yaml.safe_dump(cfg, f)

        print("Created config in 'cfg/cogs.yml'")
