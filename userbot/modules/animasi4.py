from time import sleep
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, trans_cmd


@trans_cmd(pattern="sadboy(?: |$)(.*)")
async def _(event):
    zz = await edit_or_reply(event, "Pertama-tama kamu cantik")
    sleep(1)
    await zz.edit("Kedua kamu manis")
    sleep(1)
    await zz.edit("Dan yang terakhir adalah kamu bukan jodohku")
    sleep(1)
    await zz.edit("Dahlahhh.....")

    
@trans_cmd(pattern="punten(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Punten**")

# Create by myself @localheart


@trans_cmd(pattern="pantau(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Masih Ku Pantau**")

# Create by myself @localheart


@trans_cmd(pattern="idiot(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "\n╭╮╱╱╭╮"
        "\n┃╰╮╭╯┃"
        "\n╰╮╰╯╭┻━┳╮╭╮"
        "\n╱╰╮╭┫╭╮┃┃┃┃"
        "\n╱╱┃┃┃╰╯┃╰╯┃"
        "\n╱╱╰╯╰━━┻━━╯"
        "\nㅤㅤㅤ"
        "\n╭━━━╮"
        "\n┃╭━╮┃"
        "\n┃┃╱┃┣━┳━━╮"
        "\n┃╰━╯┃╭┫┃━┫"
        "\n┃╭━╮┃┃┃┃━┫"
        "\n╰╯╱╰┻╯╰━━╯"
        "\nㅤㅤㅤ"
        "\n╭━━━╮╱╭╮╱╱╱╭╮"
        "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
        "\n┃╰━━┳━╯┣┳━┻╮╭╯"
        "\n┃╭━━┫╭╮┣┫╭╮┃┃"
        "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
        "\n╰━━━┻━━┻┻━━┻━╯"
        "\nㅤㅤㅤ"
        "\n╭━╮╱╭╮"
        "\n┃┃╰╮┃┃"
        "\n┃╭╮╰╯┣━━╮"
        "\n┃┃╰╮┃┃╭╮┃"
        "\n┃┃╱┃┃┃╰╯┃"
        "\n╰╯╱╰━┻━━╯"
        "\nㅤㅤㅤ"
        "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
        "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
        "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
        "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
        "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
        "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update(
    {
        "animasi4": f"➢ **Plugin : **`animasi4`\
        \n\n ┌✯ **Command :** `{cmd}sadboy`\
        \n └✯ **Function : **Kata-kata bocah sadboy.\
        \n\n ┌✯ **Command :** `{cmd}punten`\
        \n └✯ **Function : **Mengirim Gambar Punten.\
        \n\n ┌✯ **Command :** `{cmd}pantau`\
        \n └✯ **Function : **Mengirim Gambar Pantau.\
        \n\n ┌✯ **Command :** `{cmd}idiot`\
        \n └✯ **Function : **Mengirim Gambar Idiot.\
    "
    }
)
