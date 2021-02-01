from util.config import get_config

cfg = get_config()

async def is_allowed_in_channel(ctx):

    if await is_staff(ctx): return True  # allows staff to use commands in any channel
    if ctx.channel.name.lower() in [name.lower() for name in cfg['Allowed_Channels']]: return True
    return False

async def is_staff(ctx):

    for staff_role in cfg['Staff_Roles']:

        if staff_role.lower() in [r.name.lower() for r in ctx.author.roles]: return True

    return False