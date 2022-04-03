# Credits: @mrismanaziz
# Recode by @RYUUSHINNI

import os
from pathlib import Path

from userbot import CMD_HELP
from userbot.utils import edit_or_reply, load_module, trans_cmd, remove_plugin, reply_id


@trans_cmd(pattern="install$")
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            xx = await edit_or_reply(event, "`Installing Modules...`")
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "userbot/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await xx.edit(
                    f"**Plugin** `{os.path.basename(downloaded_file_name)}` **Berhasil di install**"
                )
                
            else:
                os.remove(downloaded_file_name)
                await xx.edit("**Error!** Plugin ini sudah terinstall di userbot.")
        except Exception as e:
            await xx.edit(str(e))
            os.remove(downloaded_file_name)


@trans_cmd(pattern="psend ([\s\S]*)")
async def send(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./userbot/modules/{input_str}.py"
    if os.path.exists(the_plugin_file):
        await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            thumb="userbot/resources/logo.jpg",
            allow_cache=False,
            reply_to=reply_to_id,
            caption=f"➠ **Nama Plugin:** `{input_str}`",
        )
        await event.delete()
    else:
        await edit_or_reply(event, "**ERROR: Modules Tidak ditemukan**")


@trans_cmd(pattern="uninstall (?P<shortname>\w+)")
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./userbot/modules/{shortname}.py"
    xx = await edit_or_reply(event, "`Processing...`")
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**Berhasil Menghapus Modules** `{shortname}`")
    except OSError as e:
        await xx.edit(f"**ERROR:** `{dir_path}` : {e.strerror}")


CMD_HELP.update(
    {
        "core": "**Plugin : **`core`\
        \n\n  •  **Syntax :** `.install` <reply ke file module>\
        \n  •  **Function : **Untuk Menginstall module userbot secara instan.\
        \n\n  •  **Syntax :** `.uninstall` <nama module>\
        \n  •  **Function : **Untuk Menguninstall / Menghapus module userbot secara instan.\
        \n\n  •  **Syntax :** `.psend` <nama module>\
        \n  •  **Function : **Untuk Mengirim module userbot secara instan.\
    "
    }
)
