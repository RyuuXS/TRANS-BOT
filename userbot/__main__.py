# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Ported by @mrizmanaziz
# FROM Man-Userbot
# ReCode by @RYUUSHINNI
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from pytgcalls import idle
from userbot import BOTLOG_CHATID, BOT_TOKEN, BOT_VER
from userbot import CMD_HANDLER as cmd
from userbot import LOGS, bot, call_py
from userbot.modules import ALL_MODULES
from userbot.modules.misc import branch
from userbot.utils import autopilot, autobot, checking

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklistman = requests.get(
        "https://raw.githubusercontent.com/RyuuXS/Reforestation/master/shinblacklist.json"
    ).json()
    if user.id in blacklistman:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @RYUUSHINNI"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())
    
LOGS.info(.
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/helpforRYUU")
LOGS.info(
    f"✨TRANS-Userbot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "✨ **Trⱥภs͢͢͢ 𝕌𝔅0T Berhasil Diaktifkan**!!\n━━━━━━━━╾╼╾╼╾╼╾╼╍\n➠ **Userbot Version** - 1.2@TRANS-BOT\n➠ **Ketik** `.ping` **Untuk Mengecheck Bot**\n━━━━━━━━━╼╾╼╾╼╳\n➠ **Powered By:** @Belajarbersamaryuu ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    
bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
   
