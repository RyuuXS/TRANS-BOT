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
from telethon.tl.functions.channels import JoinChannelRequest as kontol
from telethon.tl.functions.channels import InviteToChannelRequest as memek
from pytgcalls import idle
from userbot import (
    BOTLOG_CHATID,
    BOT_USERNAME,
    BOT_TOKEN,
    BOT_VER,
    LOGS,
    bot,
    call_py,
)
from userbot import LOGS, bot, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autopilot, autobot, checking

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklisttrans = requests.get(
        "https://raw.githubusercontent.com/RyuuXS/Reforestation/master/shinblacklist.json"
    ).json()
    if user.id in blacklisttrans:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @RYUUSHINNI"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/helpforRYUU"
)

LOGS.info(f"🔥 TRANS-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

async def trans_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"✨ **Trⱥภs͢͢͢ 𝕌𝔅0T Berhasil Diaktifkan**!!\n━━━━━━━━╾╼╾╼╾╼╾╼╍\n➠ **Userbot Version** - 1.2 @TRANS-BOT\n➠ **Ketik** `.ping` **Untuk Mengecheck Bot**\n━━━━━━━━━╼╾╼╾╼╳\n➠ **Powered By:** @Belajarbersamaryuu ",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(memek(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass          
    try:
        await bot(kontol("@helpforRYUU"))
    except BaseException:
        pass


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(trans_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
