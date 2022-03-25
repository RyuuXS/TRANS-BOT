# FROM TRANS-BOT <https://github.com/RyuuXS/TRANS-BOT>
# t.me/helpforRYUU & t.me/Belajarbersamaryuu
# ⚠️ JANGAN HAPUS CREDIT INI !!

import os

import heroku3

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME, GCAST_BLACKLIST
from userbot.utils import edit_delete, edit_or_reply, trans_cmd


Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("GCAST_BLACKLIST") or ""

@trans_cmd(pattern="blgcast$")
async def sudo(event):
    blch = "True" if GCAST_BLACKLIST else "False"
    blc = blchat
    list = blc.replace(" ", "\n• ")
    if blch == "True":
        await edit_or_reply(
            event,
            f"🚫 **GCast Blacklist :** `Enabled`\n\n📜 ** Blacklist Group :**\n• `{list}`\n\nKetik `.addblacklist` di grup untuk menambahkan ke Blacklist.",
        )
    else:
        await edit_delete(event, "🚫 **GCast Blacklis :** `Disabled`")
        

@trans_cmd(pattern="addblacklist(?:\s|$)([\s\S]*)")
async def add(event):
    xx = await edit_or_reply(event, "`Processing...`")
    var = "GCAST_BLACKLIST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blchat = f"{GCAST_BLACKLIST} {gc}"
    nenwbl = blchat.replace("{", "")
    nenwbl = nenwbl.replace("}", "")
    blcht = nenwbl.replace(",", "")
    gcastblc = blcht.replace("[", "")
    gcid = gcastblc.replace("]", "")
    gcast_blc = gcid.replace("set() ", "")
    await xx.edit(
        f"**Berhasil Menambahkan** `{gc}` **ke Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = gcast_blc
    
    
@trans_cmd(pattern="delblacklist(?:\s|$)([\s\S]*)")
async def _(event):
    xx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        nenwbl = blchat.replace(gett, "")
        await xx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "GCAST_BLACKLIST"
        heroku_Config[var] = nenwbl
    else:
        await edit_delete(
            xx, "**Pengguna ini tidak ada dalam Daftar GCast Blacklist.**", 45
        )
        
        
CMD_HELP.update(
    {
        "gcastblacklist": f"➢ **Plugin : **`gcastblacklist`\
        \n\n ┍⊛ **Command :** `{cmd}addblacklist`\
        \n ┕⊛ **Function : *Untuk menambah blacklist Gcast kalian\
        \n\n ┍⊛ **Command :** `{cmd}delblacklist`\
        \n ┕⊛ **Function : **Untuk mengurangi blacklist Gcast kalian\
        \n\n ┍⊛ **Command :** `{cmd}blgcast`\
        \n ┕⊛ **Function : **Untuk melihat info blacklist gcast Kalian.\
    "
    }
)
