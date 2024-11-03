from cybervpn import *
import subprocess
import json
import re
import base64
import datetime as DT
import requests
import time
import random
import asyncio
import tempfile
################

@bot.on(events.CallbackQuery(data=b'create-noobz-member'))
async def create_noobz(event):
    async def create_noobz_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = (await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text


        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**password:**')
            Quota = (await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text



        await process_user_balance_ssh(event, user_id)
        cmd = f'printf "%s\n" "{user}" "{Quota}" "30" "2" | addnoobz'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(30))
        

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   ** ⟨🔸Noobzvpn Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host:** `{DOMAIN}`
**» Username:** `{user}`
**» Password:** `{Quota}`
**» limit ip:** `2`
**» Harga akun:** `RP.10.000`
**» Sisa saldo:** `RP.{get_saldo_from_db(user_id)}` 
**◇━━━━━━━━━━━━━━━━━◇**
**» TCP_STD PORT     :** `8080`
**» TCP_SSL PORT    :** `8443`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Payload WS  ⟩**
`GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Akun User:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore
        """

        await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await create_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


#############


# TRIAL NOOBZVPNS
@bot.on(events.CallbackQuery(data=b'trial-noobz-member'))
async def trial_noobz(event):
    user_id = str(event.sender_id)
    async def trial_noobz_(event):
        user = "trialX" + str(random.randint(100, 1000))
        pw = "1"
        exp = "1"
        ip = "1"
        
        

        cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" "{ip}" | addnoobz'
        try:
            subprocess.check_output(cmd, shell=True)
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(exp))
            msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   ** ⟨🔸Noobzvpn Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host:** `{DOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**» limit ip:** `{ip}`
**◇━━━━━━━━━━━━━━━━━◇**
**» TCP_STD PORT     :** `8080`
**» TCP_SSL PORT    :** `8443`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Payload WS  ⟩**
```GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]```
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Akun User:** `1 hari`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore
"""
            inline = [
                [Button.url("𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖", "t.me/Riswanvpnstore"),
                 Button.url("𝚆𝚑𝚊𝚝𝚜𝚊𝚙𝚙", "wa.me/6285888801241")]
            ]
            await event.respond(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await trial_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak...!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


#############


@bot.on(events.CallbackQuery(data=b'cek-noobz-member'))
async def cek_vmess(event):
    async def cek_noobz_(event):
        cmd = 'cek-noobz'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
**◇━━━━━━━━━━━━━━━━━━◇**
   ** ⟨🔸Cek Noobz Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━━◇**
{z}

**Shows Users noobzvpns in databases**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "noobzvpns-member")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await cek_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



##########











@bot.on(events.CallbackQuery(data=b'renew-noobz-member'))
async def ren_vmess(event):
    async def ren_noobz_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**PERHATIAN!! renew akun akan memotong saldo kalian sesuai harga create account**')
            await event.respond('**Username:**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text


            

        await process_user_balance_ssh(event, user_id)   
        cmd = f'noobzvpns --renew-user {user} --expired-user {user} 30'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed  {user} 30 Days price IDR.10.000**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await ren_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

		


















@bot.on(events.CallbackQuery(data=b'noobzvpn-member'))
async def vmess(event):
    async def vmess_(event):
        inline = [
            [Button.inline(" 𝚃𝚁𝙸𝙰𝙻 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "trial-noobz-member"),
             Button.inline(" 𝙲𝚁𝙴𝙰𝚃𝙴 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽 ", "create-noobz-member")],
            [Button.inline(" 𝚁𝙴𝙽𝙴𝚆 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "renew-noobz-member")],

            [Button.inline(" 𝙲𝙷𝙴𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "cek-noobz-member")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨🔸NOOBZVPNS SERVICE🔸⟩◇**
             **Admin Manager**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `NOOBZVPNS`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore
"""
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


