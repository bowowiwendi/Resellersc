from cybervpn import *
import subprocess
import datetime as DT
import sys
from telethon.sync import TelegramClient
import sqlite3
import random

@bot.on(events.CallbackQuery(data=b'trial-ssh-member'))
async def trial_ssh(event):
    user_id = str(event.sender_id)
    async def trial_ssh_(event):
        user = "Trial-" + str(random.randint(100, 1000))
        pw = "1"
        exp = "1"
        ip = "1"
        
        with open(f'/etc/lunatic/limit/ssh/ip/{user}', 'w') as file:
            file.write(ip)
    	
        cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
        try:
            subprocess.check_output(cmd, shell=True)
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(exp))
            msg = f"""
◇━━━━━━━━━━━━━━━━━━━━━━━◇
      ** ⟨🔸𝚃𝚛𝚒𝚊𝚕 𝚂𝚂𝙷  𝙰𝚌𝚌𝚘𝚞𝚗𝚝🔸⟩**
◇━━━━━━━━━━━━━━━━━━━━━━━◇
» 𝙳𝚘𝚖𝚊𝚒𝚗: `{𝙳𝙾𝙼𝙰𝙸𝙽}`
» 𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎: `{user.strip()}`
» 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍: `{pw.strip()}`
◇━━━━━━━━━━━━━━━━━━━━━━━◇
**⟨FORMAT HTTP COSTUM⟩**
`{DOMAIN}:1-65535@{user.strip()}:{pw.strip()}`
◇━━━━━━━━━━━━━━━━━━━━━━━◇
**⟨𝙿𝚊𝚢𝚕𝚘𝚊𝚍 𝚆𝚎𝚋𝚜𝚘𝚌𝚔𝚎𝚝⟩**
```GET /cdn-cgi/trace HTTP/1.1[crlf]Host: Bug_Kalian[crlf][crlf]GET-RAY / HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]```
◇━━━━━━━━━━━━━━━━━━━━━━━◇
» 𝙴𝚡𝚙𝚒𝚛𝚎𝚍 𝚄𝚗𝚝𝚒𝚕: {𝚕𝚊𝚝𝚎𝚛}
◇━━━━━━━━━━━━━━━━━━━━━━━◇
**» ** 🤖@Riswanvpnstore
"""
            inline = [
                [Button.url("[ Contact ]", "t.me/Riswanvpnstore"),
                 Button.url("[ whatsap ]", "wa.me/6285888801241")]
            ]
            await event.respond(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await trial_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak...!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

