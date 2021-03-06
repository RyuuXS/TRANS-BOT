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
    pong = await edit_or_reply(event, "**γβππππππγ**")
    await pong.edit("**ββπππππππββ**")
    await pong.edit("**ππππππππ ππππ πππ πππ**")
    await pong.edit("**β¬ππππ πππππππ ππππππππ πππβ¬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**β² πΊπΎπ½ππΎπ» πΌπ΄π»π΄π³ππΆ** "
        f"\n β«Έ α΄·α΅βΏα΅α΅Λ‘ `%sms` \n"
        f"**β² π±πΈπΉπΈ πΏπ΄π»π΄π** "
        f"\n β«Έ α΄·α΅α΅α΅α΅βΏα΅γ`{owner}`γ \n" % (duration)
    )


@trans_cmd(pattern="kping(?: |$)(.*)")
async def _(event):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pong = await edit_or_reply(event, "8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8==β=D")
    await pong.edit("8=β==D")
    await pong.edit("8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8==β=D")
    await pong.edit("8=β==D")
    await pong.edit("8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8===βDπ¦")
    await pong.edit("8====Dπ¦π¦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**NGENTOT!! π**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}β±" % (duration)
    )


@trans_cmd(pattern="as(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**Assalamualaikum**")



@trans_cmd(pattern="ja(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!π₯**")

    
@trans_cmd(pattern="kimak(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Hallo KIMAAKK SAYA {owner}**")
    sleep(2)
    await xx.edit("**LU SEMUA NGENTOT π₯**")


@trans_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Salam Dulu Biar Sopan**")
    sleep(2)
    await xx.edit("**Ψ§ΩΨ³ΩΩΩΨ§ΩΩΩ ΨΉΩΩΩΩΩΩΩΩΩ ΩΩΨ±ΩΨ­ΩΩΩΨ©Ω Ψ§ΩΩΩΩ ΩΩΨ¨ΩΨ±ΩΩΩΨ§ΨͺΩΩΩ**")

    
CMD_HELP.update(
    {
        "gabut": f"β’ **Plugin : **`gabut`\
        \n\n ββ― **Command :** `{cmd}keping`\
        \n ββ― **Funcβ―ion : **Untuk mengeluarkan bacotan anak kampang\
        \n\n ββ― **Command :** `{cmd}kping`\
        \n ββ― **Function : **untuk ping userbot dengan awalan coli kampang\
        \n\n ββ― **Command :** `{cmd}as`\
        \n ββ― **Function : **untuk mengeluarkan salam sopan\
        \n\n ββ― **Command :** `{cmd}ass`\
        \n ββ― **Function : **untuk mengeluarkan salam Agama ISLAM\
        \n\n ββ― **Command :** `{cmd}ja`\
        \n ββ― **Function : **untuk membacot nyuruh nimbrung\
        \n\n ββ― **Command :** `{cmd}kimak`\
        \n ββ― **Function : **untuk menghina dengan kata kata kimak.\
    "
    }
)
