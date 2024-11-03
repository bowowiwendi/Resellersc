from cybervpn import *
import requests
import subprocess
@bot.on(events.CallbackQuery(data=b'create-trojan-member'))
async def create_trojan(event):
    async def create_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond("**Choose Expiry Day**", buttons=[
                [
                 Button.inline(" 30 Day ", "30")]
            ])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")

        # jumlah ip
        async with bot.conversation(chat) as ip:
            await event.respond("**Choose ip limit**", buttons=[
                [
                 Button.inline(" 2 IP ", "2")]
            ])
            ip = ip.wait_event(events.CallbackQuery)
            ip = (await ip).data.decode("ascii")
        
        await process_user_balance_trojan(event, user_id)

        await event.edit("`Wait.. Setting up an Account`")
        cmd = f'printf "%s\n" "{user}" "{exp}" "100" "{ip}" | addtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)", a)]
        print(b)
        domain = re.search("@(.*?):", b[0]).group(1)
        uuid = re.search("trojan://(.*?)@", b[0]).group(1)
        msg = f"""
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
                   **⟨🔸Trojan Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» HOST SERVER :** `{DOMAIN}`
**» USERNAME :** `{user.strip()}`
**» Port TLS  :** `443, 400-900`
**» Port NTLS :** `80, 8080, 8081-9999 `
**» UUID :** `{uuid}`
**» NetWork :** `(WS) or (gRPC)`
**» Path :** `/trojan`
**» ServiceName :** `trojan-grpc`
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{𝚋[0]}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{𝚋[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{𝚋[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
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
            await create_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'cek-tr-member'))
async def cek_trojan(event):
    async def cek_trojan_(event):
        cmd = 'cek-tr'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

**◇━━━━━━━━━━━━━━━━━━◇**
   ** ⟨🔸Cek Trojan Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━━◇**
{z}

**Shows Logged In Users Trojan**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await cek_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'trial-trojan-member'))
async def trial_trojan(event):
    async def trial_trojan_(event):
        cmd = f'printf "%s\n" "trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "2" "1" | addtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(1))
            b = [x.group() for x in re.finditer("trojan://(.*)", a)]
            print(b)
            remarks = re.search("#(.*)", b[0]).group(1)
            domain = re.search("@(.*?):", b[0]).group(1)
            uuid = re.search("trojan://(.*?)@", b[0]).group(1)
            msg = f"""
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
              **⟨🔸Trial Trojan Account🔸⟩**
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» HOST SERVER :** `{DOMAIN}`
**» Port TLS  :** `443, 400-900`
**» Port NTLS  :** `80, 8080, 8081-9999 `
**» UUID :** `{uuid}`
**» NetWork  :** `(WS) or (gRPC)`
**» Path   :** `/trojan`
**» ServiceName :** `trojan-grpc`
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL TLS    :**
```{𝚋[0]}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL HTTP    :**
```{𝚋[1].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» URL gRPC   :** 
```{𝚋[2].𝚛𝚎𝚙𝚕𝚊𝚌𝚎(" ","")}```
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━━━━━━━━━◇**
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
            await trial_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'renew-trojan-member'))
async def ren_trojan(event):
    async def ren_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Perhatian! renew akun akan mengenakan biaya sesuai create account')
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond("**Choose Expiry Day**", buttons=[
                [Button.inline(" 30 Day ", "30")]
            ])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")

        async with bot.conversation(chat) as ip:
            await event.respond("**Choose ip limit**", buttons=[
                [Button.inline(" 2 ip ", "2")]
            ])
            ip = ip.wait_event(events.CallbackQuery)
            ip = (await ip).data.decode("ascii")

        await process_user_balance_trojan(event, user_id)
        cmd = f'printf "%s\n" "{user}" "{exp}" "100" "{ip}" | renewtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed {user} {exp} days limit ip {ip} limit Quota 100GB**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await ren_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak...!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')



# CEK member tr
@bot.on(events.CallbackQuery(data=b'cek-membertr-member'))
async def cek_tr(event):
    async def cek_tr_(event):
        cmd = 'bash cek-mts'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

{z}

**Shows Users from databases**
""", buttons=[[Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await cek_tr_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


		
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
	async def delete_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | deltr'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trojan-member'))
async def trojan(event):
    async def trojan_(event):
        inline = [
            [Button.inline("𝚃𝚛𝚒𝚊𝚕 𝚃𝚛𝚘𝚓𝚊𝚗", "trial-trojan-member"),
             Button.inline("𝙲𝚛𝚎𝚊𝚝𝚎 𝚃𝚛𝚘𝚓𝚊𝚗", "create-trojan-member")],
            [Button.inline("𝙲𝚑𝚎𝚌𝚔 𝙻𝚘𝚐𝚒𝚗 𝚃𝚛𝚘𝚓𝚊𝚗", "cek-tr-member"),
             Button.inline("𝚁𝚎𝚗𝚎𝚠 𝚃𝚛𝚘𝚓𝚊𝚗", "renew-trojan-member")],
            [Button.inline("𝙲𝚑𝚎𝚌𝚔 𝙼𝚎𝚖𝚋𝚎𝚛", "cek-membertr-member")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
  **◇⟨🔸TROJAN SERVICE🔸⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `TROJAN`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» ** 🤖@Riswanvpnstore
**◇━━━━━━━━━━━━━━━━━◇**
        """
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await trojan_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

