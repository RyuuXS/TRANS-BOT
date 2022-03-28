#by @RYUUSHINNI

import time
from datetime import datetime
from platform import uname
from time import sleep

from userbot import ALIVE_NAME, StartTime
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import owner
from userbot.utils import edit_or_reply, trans_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@trans_cmd(pattern="keping(?: |$)(.*)")
async def _(event):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pong = await edit_or_reply(event, "**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await pong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await pong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await pong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
        f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
        f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "
        f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『`{owner}`』 \n" % (duration)
    )


@trans_cmd(pattern="kping(?: |$)(.*)")
async def _(event):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pong = await edit_or_reply(event, "8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**NGENTOT!! 🖕**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}⏱" % (duration)
    )


@trans_cmd(pattern="as(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**Assalamualaikum**")



@trans_cmd(pattern="ja(?: |$)(.*)")
async def _(event):
    await event.edit("**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await event.edit("**NIMBRUNG GOBLOKK!!!🔥**")

    


@trans_cmd(pattern="kimak(?: |$)(.*)")
async def _(event):
    await event.edit(f"**Hallo KIMAAKK SAYA {owner}**")
    sleep(2)
    await event.edit("**LU SEMUA NGENTOT 🔥**")




@trans_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    await event.edit("**Salam Dulu Biar Sopan**")
    sleep(2)
    await event.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")

    
CMD_HELP.update(
    {
        "gabut": f"➢ **Plugin : **`gabut`\
        \n\n ┌✯ **Command :** `{cmd}keping`\
        \n └✯ **Func✯ion : **Untuk mengeluarkan bacotan anak kampang\
        \n\n ┌✯ **Command :** `{cmd}kping`\
        \n └✯ **Function : **untuk ping userbot dengan awalan coli kampang\
        \n\n ┌✯ **Command :** `{cmd}as`\
        \n └✯ **Function : **untuk mengeluarkan salam sopan\
        \n\n ┌✯ **Command :** `{cmd}ass`\
        \n └✯ **Function : **untuk mengeluarkan salam Agama ISLAM\
        \n\n ┌✯ **Command :** `{cmd}ja`\
        \n └✯ **Function : **untuk membacot nyuruh nimbrung\
        \n\n ┌✯ **Command :** `{cmd}kimak`\
        \n └✯ **Function : **untuk menghina dengan kata kata kimak.\
    "
    }
)
