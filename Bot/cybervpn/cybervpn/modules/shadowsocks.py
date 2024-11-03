from cybervpn import *
import requests
import time
import subprocess
@bot.on(events.CallbackQuery(data=b'create-shadowsocks'))
async def create_shadowsocks(event):
    user_id = str(event.sender_id)

    async def create_shadowsocks_(event):
        try:
            async with bot.conversation(chat) as user_conv:
                await event.respond('**Username:**')
                user_msg = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                user = (await user_msg).raw_text

            async with bot.conversation(chat) as exp_conv:
                await event.respond('**expired days?:**')
                exp_msg = exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                exp = (await exp_msg).raw_text

            await event.edit("Processing.")
            await event.edit("Processing..")
            await event.edit("Processing...")
            await event.edit("Processing....")
            time.sleep(1)
            await event.edit("`Processing Create Premium Account`")
            time.sleep(1)
            await event.edit("`Wait.. Setting up an Account`")

            

            cmd = f'printf "%s\n" "{user}" "{exp}" | addss'

            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**⟨🔸SHDWSCSK Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host Server :** `{DOMAIN}`
**» Port TLS    :** `443, 400-900`
**» Port NTLS   :** `80, 8080, 8081-9999 `
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP   :** 
```{x[1].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
»  🤖@Riswanvpnstore

        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await create_shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')









@bot.on(events.CallbackQuery(data=b'cek-shadowsocks'))
async def cek_shadowsocks(event):
    user_id = str(event.sender_id)
    async def cek_shadowsocks_(event):
        cmd = 'bash cek-mss'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}

**Shows Users Shadowsocks in database**
        """, buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')




@bot.on(events.CallbackQuery(data=b'cek-shadowsocks-online'))
async def cek_shadowsocks(event):
    user_id = str(event.sender_id)
    async def cek_shadowsocks_(event):
        cmd = 'bash cek-ss'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}

**Shows online Users Shadowsocks**
        """, buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')



















@bot.on(events.CallbackQuery(data=b'delete-shadowsocks'))
async def delete_shadowsocks(event):
    async def delete_shadowsocks_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user_event = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user_text = (await user_event).raw_text

        cmd = f'printf "%s\n" "{user_text}" | delss'
        try:
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**User Not Found**")
        else:
            msg = "**Successfully Deleted**"
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(sender.id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')







@bot.on(events.CallbackQuery(data=b'trial-shadowsocks'))
async def trial_shadowsocks(event):
    user_id = str(event.sender_id)
    async def trial_shadowsocks_(event):
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(1)
        await event.edit("`Processing Crate Premium Account`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        # ... (other progress edits)
        time.sleep(1)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")

        try:
            # Assuming this function checks and processes user balance for SSH
            cmd = f'printf "%s\n" "Trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" | addss'
            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(1))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**⟨🔸Trial SHDWSCSK Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host Server :** `{DOMAIN}`
**» Port TLS    :** `443, 400-900`
**» Port NTLS   :** `80, 8080, 8081-9999 `
**» UUID    :** `{uuid}`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{x[0]}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL HTTP   :** 
```{x[1].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{x[2].replace(" ","")}```
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ** 🤖@Riswanvpnstore

        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await trial_shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')










@bot.on(events.CallbackQuery(data=b'renew-ss'))
async def ren_ss(event):
    async def ren_ss_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            

        cmd = f'printf "%s\n" "{user}" "{exp}" | renew-ss'

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
            await ren_ss_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')







@bot.on(events.CallbackQuery(data=b'shadowsocks'))
async def shadowsocks(event):
    user_id = str(event.sender_id)

    async def shadowsocks_(event):
        inline = [
            [Button.inline("𝚃𝚛𝚒𝚊𝚕 𝚂𝚑𝚍𝚠𝚜𝚔", "trial-shadowsocks"),
             Button.inline("𝙲𝚛𝚎𝚊𝚝𝚎 𝚂𝚑𝚍𝚠𝚜𝚔", "create-shadowsocks")],
            [Button.inline("𝙲𝚎𝚔 𝚂𝚑𝚍𝚠𝚜𝚔", "cek-shadowsocks")],
            [Button.inline("𝙲𝚎𝚔 𝚄𝚜𝚎𝚛 𝙾𝚗𝚕𝚒𝚗𝚎", "cek-shadowsocks-online")],
[Button.inline("𝚁𝚎𝚗𝚎𝚠 𝚄𝚜𝚎𝚛", "renew-ss")],
[Button.inline("𝙷𝚊𝚙𝚞𝚜 𝚂𝚑𝚍𝚠𝚜𝚔", "delete-shadowsocks")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]]
        
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⟨🔸SHDWSK MANAGER🔸⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
» Service: `SHADOWSOCKS`
» Hostname/IP: `{DOMAIN}`
» ISP: `{z["isp"]}`
» Country: `{z["country"]}`
**» ** 🤖@Riswanvpnstore
**◇━━━━━━━━━━━━━━━━━◇**
"""

        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


