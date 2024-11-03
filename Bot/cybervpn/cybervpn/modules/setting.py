from cybervpn import *
import requests
import subprocess
import time
import os
@bot.on(events.CallbackQuery(data=b'reboot'))
async def reboot(event):
    user_id = str(event.sender_id)
    async def reboot_(event):
        cmd = 'reboot'
        subprocess.check_output(cmd, shell=True)
        await event.edit("""
**» REBOOT SERVER**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await reboot_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'resx'))
async def resx(event):
    user_id = str(event.sender_id)
    async def resx_(event):
        cmd = 'restart'
        subprocess.check_output(cmd, shell=True)
        await event.edit("""
**» Restarting Service Done**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await resx_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')

		
@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
    user_id = str(event.sender_id)
    async def speedtest_(event):
        cmd = 'speedtest-cli --share'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        time.sleep(0)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        await event.respond(f"""
**
{z}
**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await speedtest_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'backup'))
async def backup(event):
    user_id = str(event.sender_id)
    async def backup_(event):
        cmd = 'printf "%s\n" | bot-backup'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Not Exist**")
        else:
            msg = f"```\nfile backupmu Bro\n```"
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await backup_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'rest'))
async def upload(event):
    user_id = str(event.sender_id)
    async def upload_(event):
        me = await bot.get_me()
        async with bot.conversation(event.chat_id) as con:
            await event.reply('**Upload File:**')
            file = con.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            file = await file
            file = file.message.media
            file = await event.client.download_media(file, "/root/folder")
            path = file
            sex = "mrestore"
            ox = subprocess.check_output(sex, shell=True).decode("utf-8")
            msg = f"{ox}"

        await event.respond("`Please Wait Proccess Restored`".format(os.path.basename(file)))
        await event.respond(msg, buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await upload_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')



@bot.on(events.NewMessage(pattern="(?:.restore|/restore)"))
async def rest(event):
    user_id = str(event.sender_id)
    db = get_db()

    async def rest_(event):
        if event.is_reply:
            try:
                restore = await event.client.download_media(
                    await event.get_reply_message(),
                    "cybervpn/",
                )

                if "(" not in restore:
                    path1 = Path(restore)
                    await event.respond(
                        "Uploaded To Server `{}`".format(
                            os.path.basename(restore)
                        )
                    )
                    owe = subprocess.check_output(restorebot, shell=True)
                    await event.respond(f"{owe}", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])
                else:
                    os.remove(restore)
                    await event.respond("Restore Data Failed")
            except Exception as e:
                await event.respond(str(e))
                os.remove(restore)

        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await rest_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')



@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
    user_id = str(event.sender_id)
    async def backers_(event):
        inline = [
            [Button.inline("𝙱𝚊𝚌𝚔𝚞𝚙", "backup"), Button.inline(" RESTORE", "rest")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━◇**
**◇⟨🔸BACKUP & RESTORE🔸⟩◇**
                   **SERVICE**
**◇━━━━━━━━━━━━━━━━◇**
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore
"""
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await backers_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
    user_id = str(event.sender_id)
    async def settings_(event):
        inline = [
            [Button.inline("𝚂𝚙𝚎𝚎𝚍𝚝𝚎𝚜𝚝", "speedtest"), Button.inline(" BACKUP & RESTORE", "backer")],
[Button.inline("𝙴-𝚠𝚊𝚕𝚕𝚎𝚝 𝚂𝚎𝚝𝚝𝚒𝚗𝚐", "ewallet")],
            [Button.inline("𝚁𝚎𝚋𝚘𝚘𝚝 𝚂𝚎𝚛𝚟𝚎𝚛", "reboot"), Button.inline(" RESTART SERVICE", "resx")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━◇**
  **◇⟨🔸OTHER SETTING🔸⟩◇**
                 **SERVICE**
**◇━━━━━━━━━━━━━━━━◇**
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore
"""
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await settings_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')

