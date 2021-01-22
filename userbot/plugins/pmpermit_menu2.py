"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No Name set yet. [KSATHON.](t.me/KSATHON)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """

    await alive.edit("⌔︙ TeleThon For KSA \n"
                     "⌔︙ Version: 1.0.0\n"
                     "⌔︙ Created By : [© By Team #Ksathon™](https://t.me/KSATHON)\n"
                     "⌔︙ Python Tools : @TweakPY\n"
                    f"⌔︙ My Dev : [@BERŁN] (https://t.me/berliv)\n")

    
