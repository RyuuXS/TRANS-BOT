# Β© @JustRex Xa-Userbot
# I took these modules from ultroid and modified them
# Jangan hapus yg ada tanda # kontol!

import asyncio

from userbot.utils import edit_or_reply, trans_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


#creted by @JustRex

@trans_cmd(pattern="lebaran(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await edit_or_reply(event, 'πΊππππππ π―πππ πΉπππ π°πππ π­ππππ')
    animation_chars = [
        '[Happy Eid Mubarak ](https://telegra.ph/file/f950e09cc4aebcf2abe7f.jpg)',
        '[Β­π](https://telegra.ph/file/506f5aa4870472307f8fd.jpg)',
        '[γ€Β­](https://telegra.ph/file/759966f82f6590a1b8dfa.jpg)',
        '[Β­γ€](https://telegra.ph/file/661ca99916b9cf5a582d6.jpg)',
        '[γ€](https://telegra.ph/file/8bec6bbe35d4bd1587569.jpg)',
        '[π](https://telegra.ph/file/360ce99e861f8efca1ea3.jpg)',
        '[β£οΈ](https://telegra.ph/file/701503c243265b40e3223.jpg)',
        '[β€οΈ](https://telegra.ph/file/9f0f76eeba3e54298d60a.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await edit_or_reply(event, animation_chars[i % 8], link_preview=True)


@trans_cmd(pattern="hbd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await edit_or_reply(event, 'π»ππππ¦ π΅πππ‘ππππ¦')
    animation_chars = [
        '[π»ππππ¦ ](https://telegra.ph/file/2fbc53ea22ec4471929fa.jpg)',
        '[Β­πππ](https://telegra.ph/file/e4e5729634f5c8c0c9e06.jpg)',
        '[π΅πππ‘ππππ¦ππ](https://telegra.ph/file/d60d1697b9ac267371fd6.jpg)',
        '[Β­ππ πππ’π](https://telegra.ph/file/0a5d688271f8259b43a9f.jpg)',
        '[π»ππππ¦ π΅πππ‘ππππ¦ππ](https://telegra.ph/file/2fd7cf79f3478ee3c9a27.jpg)',
        '[ππ](https://telegra.ph/file/0f39e15093b70d3502bda.jpg)',
        '[ππππ](https://telegra.ph/file/59d6d8e8b1b9d3b112fc3.jpg)',
        '[πππ](https://telegra.ph/file/8021015799addb650f107.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await edit_or_reply(event, animation_chars[i % 8], link_preview=True)


@trans_cmd(pattern="happyaniv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await edit_or_reply(event, 'π»ππππ¦ π΄πππ£πππ πππ¦')
    animation_chars = [
        '[π»ππππ¦ ](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[β€οΈβ€οΈβ€οΈ](https://telegra.ph/file/ebc83df798ba99a94bfc3.jpg)',
        '[π΄πππ£πππ πππ¦β€οΈβ€οΈ](https://telegra.ph/file/1a302daf9ac95e931b675.jpg)',
        '[Β­ππ¦ πππππ©ββ€οΈβπβπ¨](https://telegra.ph/file/8a1cba2ab4bbd86609a68.jpg)',
        '[π»ππππ¦ π΄πππ£πππ πππ¦π»ππ](https://telegra.ph/file/88a297c386c0c2f999e9c.jpg)',
        '[β€οΈβ€οΈππ](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[πππβ€οΈ](https://telegra.ph/file/59ca0bbaeb740ee58aa72.jpg)',
        '[πππ](https://telegra.ph/file/3cd166b4057b5b60aa71d.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await edit_or_reply(event, animation_chars[i % 8], link_preview=True)
        
#created by @greyysbss

@trans_cmd(pattern="funcat(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await edit_or_reply(event, 'ππͺπ£ πΎππ© π πΏ πΎ')
    animation_chars = [
        '[π πΏ πΎ](https://telegra.ph/file/b7de6dd33a9d8276ebaa1.jpg)',
        '[πΉ πΉ πΉ](https://telegra.ph/file/1c3da2a4dae56b175d344.jpg)',
        '[πΌ πΌ πΌ](https://telegra.ph/file/0158811403a0027c3ba3c.jpg)',
        '[πΊ πΊ πΊ](https://telegra.ph/file/982f318a1f0dad9d1ba20.jpg)',
        '[πΌ πΌ πΌ](https://telegra.ph/file/11e60f647f23cac4d2545.jpg)',
        '[π πΏ π](https://telegra.ph/file/48939584879d9bfdbb26a.jpg)',
        '[πΏ πΏ πΏ](https://telegra.ph/file/3d539625f87a2a2b3a83b.jpg)',
        '[πΎ π πΎ](https://telegra.ph/file/b9556bb52e6077e9c98a6.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await edit_or_reply(event, animation_chars[i % 8], link_preview=True)   
        
        
CMD_HELP.update(
    {
        "ucapan": f"**β’ Plugin : **`ucapan`\
        \n\n ββ― **Syntax :** `{cmd}hbd`\
        \n ββ― **Function : **ucapan selamat ulang tahun.\
        \n\n ββ― **Syntax :** `{cmd}lebaran`\
        \n ββ― **Function : **Ucapan Lebaran.\
        \n\n ββ― **Syntax :** `{cmd}happyaniv`\
        \n ββ― **Function : **Untuk Mengucapkan Happy Aniversary kepasanganmu (Kalo Punya).\
        \n\n ββ― **Syntax :** `{cmd}funcat`\
        \n ββ― **Function : **Foto Meme Kucing."
    })        
        
        
        
