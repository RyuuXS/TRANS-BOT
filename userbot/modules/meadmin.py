# TRANS-BOT
# Copyright (C) 2022 CilikProject
#
# @RYUUSHINNI

import asyncio
import os

from userbot import bot
from userbot.utils import edit_or_reply, trans_cmd


@trans_cmd(pattern="meadmin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    here = event.chat_id
    args = event.pattern_match.group(1)
    trans = await edit_or_reply(event, "`Processing...`")
    admin_list = []
    dialogue = await bot.get_dialogs()
    for dialog in dialogue:
        if dialog.is_group or dialog.is_channel:
            ids = await bot.get_entity(dialog)
            try:
                if ids.admin_rights or ids.creator:
                    info = f"{ids.id}:  {ids.title}"
                    admin_list.append(info)
            except BaseException:
                pass
            except Exception:
                continue

    if len(admin_list) > 0:
        await trans.edit('`Berhasil, Sedang Membuat File 🖨️`')
        with open('me_admin.txt', 'w') as book:
            for groups_channels in admin_list:
                book.write(groups_channels + '\n')
        await asyncio.sleep(1)
        caption = f'List of Chats Where I have Admin Rights [total: {len(admin_list)}]'
        if args and "pv" in args:
            await bot.send_file("me", "me_admin.txt", caption=caption)
            await trans.respond("`File terkirim ke Pesan Tersimpan mu`")
        else:
            await bot.send_file(here, "me_admin.txt", caption=caption)
        os.remove("me_admin.txt")
        await event.reply("`reply ketik .carbon`")
        await trans.delete()
    else:
        await trans.edit("`Sed, I'm not Admin anywhere 🤧`")
