Mandatory Imports


There is None Mandatory Imports. Because Var, bot and command are already automatically imported.

Explanation

The Mandatory Imports are now automatically imported.

Formation
Now I will show a short script to show the formation of the desired script.

@command(pattern="^.alive", outgoing=True)
async def hello_world(event):
    if event.fwd_from:
        return
    await event.edit("**HELLO WORLD**\n\nThe following is controlling me too!\n" + Var.SUDO_USERS)