from cybervpn import *
import subprocess
import datetime as DT
import asyncio

@bot.on(events.CallbackQuery(data=b'registrasi-member'))
async def registrasi_handler(event):
    chat = event.chat_id
    sender = await event.get_sender()
    user_id = str(event.sender_id)

    async with bot.conversation(chat) as level:
        await event.edit("**Pilih Type**", buttons=[
            [Button.inline("𝙰𝚍𝚖𝚒𝚗", "admin"), Button.inline("𝚄𝚜𝚎𝚛", "user")]
        ])
        level = (await level.wait_event(events.CallbackQuery)).data.decode("ascii")

    async def registrasi_member(username, telegram_id):
        saldo = 0
        register_user(telegram_id, saldo, level)

        today = DT.date.today()
        later = today + DT.timedelta(days=int(0))
        msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ 🕊 Registration Success 🕊 ⟩**
**━━━━━━━━━━━━━━━━**
**» Member ID:** `{telegram_id}`
**» Username member:** `{username}`
**» Balance:** `IDR.0`
**━━━━━━━━━━━━━━━━**
**» Registration Date:** `{later}`
**━━━━━━━━━━━━━━━━**
"""
        inline = [
                [Button.url("𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖", "t.me/Lite_Vermilion"),
                 Button.url("𝚆𝚑𝚊𝚝𝚜𝙰𝚙𝚙", "wa.me/6281934335091")]
        ]
        await event.respond(msg, buttons=inline)

    async with bot.conversation(chat) as conv:
        try:
            # Input username
            await conv.send_message('**Input username member:**')
            user_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            username = user_msg.raw_text

            # Input Telegram ID
            await conv.send_message('**Input Telegram ID member:**')
            id_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            telegram_id = id_msg.raw_text

            await registrasi_member(username, telegram_id)

            user_level = get_level_from_db(user_id)
            print(f'Retrieved level from database: {user_level}')

            if user_level == 'admin':
                await registrasi_handler(event)
            else:
                await event.answer(f'Akses Ditolak..!!', alert=True)

        except asyncio.TimeoutError:
            print("Timeout occurred during conversation.")
            await event.respond("Percakapan timeout. Silakan coba lagi.")
        except Exception as e:
            print(f'Error: {e}')

