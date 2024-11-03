import requests
from cybervpn import *

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
    async def ssh_member_manager(event):
        inline = [
            [Button.inline("𝚃𝚛𝚒𝚊𝚕 𝚂𝚂𝙷", "trial-ssh-member"),
             Button.inline("𝙲𝚛𝚎𝚊𝚝𝚎 𝚂𝚂𝙷]", "create-ssh-member")],
            [Button.inline("𝙲𝚑𝚎𝚌𝚔 𝙻𝚘𝚐𝚒𝚗 𝚂𝚂𝙷", "login-ssh-member")],
            [Button.inline("𝚂𝚑𝚘𝚠 𝙰𝚕𝚕 𝚄𝚜𝚎𝚛 𝚂𝚂𝙷", "show-ssh-member")],
[Button.inline("𝚁𝚎𝚗𝚎𝚠 𝚂𝚂𝙷", "renew-ssh-member")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]]
        
        location_info = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━◇**
     **◇⟨🔸SSH SERVICE🔸⟩◇**
**◇━━━━━━━━━━━━━━━━◇**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{location_info["isp"]}`
**» Country:** `{location_info["country"]}`
**» ** 🤖@Riswanvpnstore
**◇━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    async def ssh_admin_manager(event):
        inline = [
            [Button.inline("𝚃𝚛𝚒𝚊𝚕 𝚂𝚂𝙷", "trial-ssh"),
             Button.inline("𝙲𝚛𝚎𝚊𝚝𝚎 𝚂𝚂𝙷", "create-ssh"),
             Button.inline("𝙳𝚎𝚕𝚎𝚝𝚎 𝚂𝚂𝙷", "delete-ssh")],
            [Button.inline("𝙲𝚑𝚎𝚌𝚔 𝙻𝚘𝚐𝚒𝚗 𝚂𝚂𝙷", "login-ssh")],
            [Button.inline("𝚂𝚑𝚘𝚠 𝙰𝚕𝚕 𝚄𝚜𝚎𝚛 𝚂𝚂𝙷", "show-ssh")],
[Button.inline("𝚁𝚎𝚗𝚎𝚠 𝚂𝚂𝙷", "renew-ssh")],
            [Button.inline("‹ 𝙼𝚊𝚒𝚗 𝙼𝚎𝚗𝚞 ›", "menu")]]
        
        location_info = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━◇**
    **◇⟨🔸SSH SERVICE🔸⟩◇**
           **Admin Manager**
**◇━━━━━━━━━━━━━━━━◇**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{location_info["isp"]}`
**» Country:** `{location_info["country"]}`
**» ** 🤖@Riswanvpnstore
**◇━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ssh_admin_manager(event)
        else:
            await ssh_member_manager(event)
    except Exception as e:
        print(f'Error: {e}')

