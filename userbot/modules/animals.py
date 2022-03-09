import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, trans_cmd


@trans_cmd(pattern="shibe$")
async def shibe(event):
    xx = await edit_or_reply(event, "`Processing...`")
    response = requests.get("https://shibe.online/api/shibes").json()
    if not response:
        await event.edit("**Tidak bisa menemukan Anjing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


@trans_cmd(pattern="cat$")
async def cats(event):
    xx = await edit_or_reply(event, "`Processing...`")
    response = requests.get("https://shibe.online/api/cats").json()
    if not response:
        await event.edit("**Tidak bisa menemukan kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


CMD_HELP.update(
    {
        "animals": f"**Plugin : **`animals`\
        \n\n  •  **Syntax :** `{cmd}cat`\
        \n  •  **Function : **Untuk Mengirim gambar kucing secara random.\
        \n\n  •  **Syntax :** `{cmd}shibe`\
        \n  •  **Function : **Untuk Mengirim gambar random dari anjing jenis Shiba.\
    "
    }
)
