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

@bot.on(events.CallbackQuery(data=b'create-noobz'))
async def create_noobz(event):
    async def create_noobz_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = (await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text


        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**password:**')
            Quota = (await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text


        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = (await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as ip_conv:
            await event.respond('**ip limit:**')
            ip = (await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text


        cmd = f'printf "%s\n" "{user}" "{Quota}" "{exp}" "{ip}" | addnoobz'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
   ** ⟨🔸Noobzvpn Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host:** `{DOMAIN}`
**» Username:** `{user}`
**» Password:** `{Quota}`
**» limit ip:** `{ip}`
**◇━━━━━━━━━━━━━━━━━◇**
**» TCP_STD PORT   :** `8080`
**» TCP_SSL PORT  :** `8443`
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

        if level == 'admin':
            await create_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


#############


# TRIAL NOOBZVPNS
@bot.on(events.CallbackQuery(data=b'trial-noobz'))
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
`GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Akun User:** `1 hari`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswnvpnstore
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

        if level == 'admin':
            await trial_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak...!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


#############


@bot.on(events.CallbackQuery(data=b'cek-noobz'))
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
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "noobzvpns")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



##########



@bot.on(events.CallbackQuery(data=b'delete-noobz'))
async def delete_noobz(event):
    async def delete_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'noobzvpns --remove-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted {user} **"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')
        

###################


@bot.on(events.CallbackQuery(data=b'block-noobz'))
async def block_noobz(event):
    async def block_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'noobzvpns --block-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully blocked {user} **"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await block_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')




###################



@bot.on(events.CallbackQuery(data=b'unblock-noobz'))
async def unblock_noobz(event):
    async def unblock_noobz_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'noobzvpns --unblock-user {user}'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully blocked {user} **"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await unblock_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')




####################


@bot.on(events.CallbackQuery(data=b'renew-noobz'))
async def ren_vmess(event):
    async def ren_noobz_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            

            
        cmd = f'noobzvpns --renew-user {user} --expired-user {user} {exp}'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed  {user} {exp} Days**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_noobz_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

		


















@bot.on(events.CallbackQuery(data=b'noobzvpns'))
async def vmess(event):
    async def vmess_(event):
        inline = [
            [Button.inline(" TRIAL 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "trial-noobz"),
             Button.inline(" 𝙲𝚁𝙴𝙰𝚃𝙴 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "create-noobz")],
            [Button.inline(" 𝙳𝙴𝙻𝙴𝚃𝙴 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "delete-noobz")],
            [Button.inline(" 𝚁𝙴𝙽𝙴𝚆 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "renew-noobz")],
            [Button.inline(" 𝙱𝙻𝙾𝙲𝙺 𝚄𝚂𝙴𝚁  ", "block-noobz"),
             Button.inline(" 𝚄𝙽𝙱𝙻𝙾𝙲𝙺 𝚄𝚂𝙴𝚁  ", "unblock-noobz")],
            [Button.inline(" 𝙲𝙷𝙴𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁 𝙽𝙾𝙾𝙱𝚉𝚅𝙿𝙽𝚂 ", "cek-noobz")],
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
**» ** 🤖@Lite_Vermilion
"""
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


