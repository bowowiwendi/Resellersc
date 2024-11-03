from cybervpn import *
from telethon import events, Button
import requests

url = "https://raw.githubusercontent.com/scriswan/fodder/main/statusku"

response = requests.get(url)


if response.status_code == 200:
    print(response.text)
else:
    print("Gagal mendapatkan konten dari URL")

@bot.on(events.NewMessage(pattern=r"(?:.menu|/start|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def start_menu(event):
    user_id = str(event.sender_id)

    if check_user_registration(user_id):
        try:
            saldo_aji, level = get_saldo_and_level_from_db(user_id)

            if level == "user":
                member_inline = [
                    [Button.inline("𝚂𝚂𝙷", "ssh")],
                    [Button.inline("𝚅𝚖𝚎𝚜𝚜", "vmess-member"),
                     Button.inline("𝚅𝚕𝚎𝚜𝚜", "vless-member")],
                    [Button.inline("𝚃𝚛𝚘𝚓𝚊𝚗", "trojan-member"),
                     Button.inline("𝚂𝚑𝚊𝚍𝚘𝚠𝚜𝚘𝚌𝚔𝚜", "shadowsocks-member")],
                    [Button.inline("𝙽𝚘𝚘𝚋𝚣𝚟𝚙𝚗𝚜", "noobzvpn-member")],
                    [Button.url("𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖", "https://t.me/Riswanvpnstore"),
                     Button.inline("𝚃𝚘𝚙𝚄𝚙", f"topup")]
                ]

                member_msg = f"""
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
 **🙎‍♂️𝗠𝗘𝗠𝗕𝗘𝗥 𝙍𝙄𝙎𝙒𝘼𝙉 𝙎𝙏𝙊𝙍𝙀 𝘽𝙊𝙏🙎‍♂️**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟭 𝗕𝗨𝗟𝗔𝗡 = 𝟭𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟮 𝗕𝗨𝗟𝗔𝗡 = 𝟮𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟯 𝗕𝗨𝗟𝗔𝗡 = 𝟯𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟰 𝗕𝗨𝗟𝗔𝗡 = 𝟰𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟱 𝗕𝗨𝗟𝗔𝗡 = 𝟱𝟬.𝟬𝟬𝟬**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**💰𝗠𝗜𝗡𝗜𝗠𝗔𝗟 𝗧𝗢𝗣𝗨𝗣 𝗥𝗣 𝟭𝟬.𝟬𝟬𝟬**
**🙎‍♂️𝗝𝗜𝗞𝗔 𝗜𝗡𝗚𝗜𝗡 𝗠𝗘𝗠𝗕𝗨𝗔𝗧 𝗔𝗞𝗨𝗡**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**🙎‍♂️𝗨𝗦𝗘𝗥 𝗜𝗗 : ** `{user_id}`**
**💰𝗦𝗔𝗟𝗗𝗢𝗠𝗨 : ** `Rp.{saldo_aji}`
**◇━━━━━━━━━━━━━━━━━━━━━━━◇
🤖@Riswanvpnstore
"""
                x = await event.edit(member_msg, buttons=member_inline)
                if not x:
                    await event.reply(member_msg, buttons=member_inline)


            elif level == "admin":
                admin_inline = [
                    [Button.inline("𝙰𝚔𝚞𝚗 𝚂𝚂𝙷", "ssh")],
                    [Button.inline("𝙰𝚔𝚞𝚗 𝚅𝚖𝚎𝚜𝚜", "vmess"),
                     Button.inline("𝙰𝚔𝚞𝚗 𝚅𝚕𝚎𝚜𝚜", "vless")],
                    [Button.inline("𝚂𝚌𝚛𝚒𝚙𝚝 𝚟𝚙𝚗", "trojan"),
                     Button.inline("𝚂𝚑𝚊𝚍𝚘𝚠𝚜𝚘𝚌𝚔𝚜", "shadowsocks")],
                    [Button.inline("𝙽𝚘𝚘𝚋𝚣𝚟𝚙𝚗𝚜", "noobzvpns"),
                     Button.inline("𝙰𝚍𝚍 𝙼𝚎𝚖𝚋𝚎𝚛", "registrasi-member"),
                     Button.inline("𝙷𝚊𝚙𝚞𝚜 𝙼𝚎𝚖𝚋𝚎𝚛", "delete-member")],
                     [Button.inline("𝙳𝚊𝚏𝚝𝚊𝚛 𝙼𝚎𝚖𝚋𝚎𝚛", "show-user")],
                    [Button.inline("𝙰𝚍𝚍 𝚂𝚊𝚕𝚍𝚘 𝚄𝚜𝚎𝚛", "addsaldo")],
                    [Button.inline("𝙲𝚑𝚎𝚌𝚔 𝚅𝚙𝚜 𝙸𝚗𝚏𝚘", "info"),
                     Button.inline("𝙾𝚝𝚑𝚎𝚛 𝚂𝚎𝚝𝚝𝚒𝚗𝚐", "setting")],
                    [Button.url("𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖", "https://t.me/Riswanvpnstore"),
                     Button.url("𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙸𝚙𝚟𝚙𝚜", "https://github.com/scriswan/lunaip/edit/main/ip")]
                ]

                admin_msg = f"""
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
           **🙎‍♂️𝙍𝙄𝙎𝙒𝘼𝙉 𝙎𝙏𝙊𝙍𝙀 𝘽𝙊𝙏🙎‍♂️**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟭 𝗕𝗨𝗟𝗔𝗡 = 𝟭𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟮 𝗕𝗨𝗟𝗔𝗡 = 𝟮𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟯 𝗕𝗨𝗟𝗔𝗡 = 𝟯𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟰 𝗕𝗨𝗟𝗔𝗡 = 𝟰𝟬.𝟬𝟬𝟬**
**🔹𝗟𝗜𝗦𝗧 𝗛𝗔𝗥𝗚𝗔 𝟱 𝗕𝗨𝗟𝗔𝗡 = 𝟱𝟬.𝟬𝟬𝟬**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**💰𝗠𝗜𝗡𝗜𝗠𝗔𝗟 𝗧𝗢𝗣𝗨𝗣 𝗥𝗣 : 𝟭𝟬.𝟬𝟬𝟬**
**🙎‍♂️𝗝𝗜𝗞𝗔 𝗜𝗡𝗚𝗜𝗡 𝗠𝗘𝗠𝗕𝗨𝗔𝗧 𝗔𝗞𝗨𝗡**
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**🙎‍♂️𝗨𝗦𝗘𝗥 𝗜𝗗 : ** `{user_id}`**
**💰𝗦𝗔𝗟𝗗𝗢𝗠𝗨 : ** `Rp.{saldo_aji}`
**◇━━━━━━━━━━━━━━━━━━━━━━━◇**
**🙎‍♂️𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥 𝗕𝗢𝗧:** `{get_user_count()}`
**◇━━━━━━━━━━━━━━━━━━━━━━━◇
🤖@Riswanvpnstore
"""
                x = await event.edit(admin_msg, buttons=admin_inline)
                if not x:
                    await event.reply(admin_msg, buttons=admin_inline)

        except Exception as e:
            print(f"Error: {e}")

    else:
        await event.reply(
            f'**Siilahkan Registrasi Terlebih Dahulu**',
            buttons=[[(Button.inline("Registrasi", "registrasi"))]]
        )

