from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, trans_cmd


@trans_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamualaikum Warohmatulohi Wabarokatu*")


@trans_cmd(pattern="^P(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamu'alaikum**")
    
@trans_cmd(pattern="^L(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Wa'alaikumsalam**")

    
@trans_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Hy kaa 🥺**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@trans_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event,f"**Astaghfirullah, Jawab salam dong**")
    sleep(2)
    await xx.edit("**Wa'alaikumsalam**")


@trans_cmd(pattern="L(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Astaghfirullah, Jawab salam dong**")
    sleep(2)
    await xx.edit("**Wa'alaikumsalam**")



CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\nㅤㅤ•**Syntax** : {cmd}p\
        \n•**Function : **Assalamualaikum Wr Wb..\
        \n\nㅤㅤ•**Syntax** : {cmd}P\
        \n•**Function : **salam Kenal dan salam\
        \n\nㅤㅤ•**Syntax** : {cmd}l\
        \n•**Function : **Untuk Menjawab salam\
        \n\nㅤㅤ•**Syntax** :{cmd}L\
        \n•**Function : **Untuk menjawab salam\
    "
    })
