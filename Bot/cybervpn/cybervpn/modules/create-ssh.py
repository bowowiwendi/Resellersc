from cybervpn import *
import subprocess
import datetime as DT
import sys
from telethon.sync import TelegramClient
import sqlite3

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
    user_id = str(event.sender_id)

    async def create_ssh_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user_msg = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user_msg).raw_text
        
        async with bot.conversation(chat) as pw_conv:
            await event.respond("**Password:**")
            pw_msg = pw_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw_msg).raw_text
        
        async with bot.conversation(chat) as exp_conv:
            await event.respond("**Expired:**", buttons=[
            [Button.inline("3 Day", "3"), Button.inline("5 Day", "5")],
[Button.inline("7 Day", "7")],
            [Button.inline("15 Day", "15"), Button.inline("30 Day", "30")],
            [Button.inline("60 Day", "60")]
        ])
            exp_msg = exp_conv.wait_event(events.CallbackQuery)
            exp = (await exp_msg).data.decode("ascii")
        
        async with bot.conversation(chat) as ip_conv:
            await event.respond("**Limit IP:**", buttons=[
            [Button.inline("2 Ip", "2"), Button.inline("4 Ip", "4")],
[Button.inline("5 Ip", "5")],
            [Button.inline("8 Ip", "8"), Button.inline("10 Ip", "10")],
            [Button.inline("15 Ip", "15")]
        ])
            ip_msg = ip_conv.wait_event(events.CallbackQuery)
            ip = (await ip_msg).data.decode("ascii")
        
        # Simpan informasi IP limit ke dalam file
        with open(f'/etc/lunatic/limit/ssh/ip/{user}', 'w') as file:
            file.write(ip)

        # Panggil fungsi untuk memproses saldo pengguna
        await process_user_balance_ssh(event, user_id)

        # Lanjutkan dengan eksekusi perintah useradd dan pesan respons
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
       ** ⟨🔸𝚂𝚂𝙷 & 𝙾𝚅𝙿𝙽 𝙰𝚌𝚌𝚘𝚞𝚗𝚝🔸⟩**
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
                [Button.url("𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖", "t.me/Riswanvpnstore"),
                 Button.url("𝚆𝚑𝚊𝚝𝚜𝙰𝚙𝚙", "wa.me/6285888801241")]
            ]
            await event.respond(msg, buttons=inline)
            
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await create_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

