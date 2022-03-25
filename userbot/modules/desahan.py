# FROM TRANS-BOT <https://github.com/RyuuXS/TRANS-BOT>
# t.me/helpforRYUU & t.me/Belajarbersamaryuu
# ⚠️ JANGAN HAPUS CREDIT INI !!

from secrets import choice

from telethon.tl.types import InputMessagesFilterVoice

from userbot import BLACKLIST_CHAT
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, trans_cmd


@trans_cmd(pattern="desahcewe$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcewe = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcewe), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cewe.**")


@trans_cmd(pattern="desahcowo$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcowo = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowokkkk", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcowo), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cowo.**")
        
        
CMD_HELP.update(
    {
        "desahan": f"➢ **Plugin : **`desahan`\
        \n\n ┍⊛ **Command :** `{cmd}desahcewe`\
        \n ┕⊛ **Function : *Untuk Mengirim voice desah cewe secara random\
        \n\n ┍⊛ **Command :** `{cmd}desahcowo`\
        \n ┕⊛ **Function : **Untuk Mengirim voice desah cowo secara random.\
    "
    }
)
