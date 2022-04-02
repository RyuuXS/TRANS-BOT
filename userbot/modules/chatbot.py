# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from userbot import (
    CMD_HANDLER as cmd,
    CMD_HELP,
    LOGS,
    bot,
)
from userbot.utils import edit_or_reply, trans_cmd
from userbot.modules.sql_helper.tede_chatbot_sql import is_tede, rem_tede, set_tede

translator = Translator()
LANGUAGE = "id"

url = "https://apitede.herokuapp.com/api/chatbot?message={message}"


async def ngapain_rep(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return (data.json())["msg"]
        else:
            LOGS.info("ERROR: API chatbot sedang down, report ke @tedesupport.")
    except Exception as e:
        LOGS.info(str(e))


async def chat_bot_toggle(event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if not is_tede(chat_id):
            set_tede(chat_id)
            return await edit_or_reply(event, "ChatBot Diaktifkan!")
        await event.edit("ChatBot Sudah Diaktifkan.")
    elif status == "off":
        if is_tede(chat_id):
            rem_tede(chat_id)
            return await edit_or_reply(event, "ChatBot Dinonaktifkan!")
        await event.edit("ChatBot Sudah Dinonaktifkan.")
    else:
        await edit_or_reply(event, "**Usage:** `.chatbot` <on/off>")


@trans_cmd(pattern="chatbot(?: |$)(.*)")
async def on_apa_off(event):
    await chat_bot_toggle(event)


@bot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned),
    ),
)
async def tede_chatbot(event):
    sender = await event.get_sender()
    if not is_tede(event.chat_id):
        return
    if not isinstance(sender, User):
        return
    if event.text:
        rep = await ngapain_rep(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)
        else:
            await event.reply(rep)

            
CMD_HELP.update(
    {
        "chatbot": f"**➢ Plugin : **`chatbot`\
      \n\n ┌✯ **Syntax :** `{cmd}chatbot` <on/off>\
      \n └✯ **Function :** Untuk membalas chat dengan chatbot AI.\
      "
    }
)
