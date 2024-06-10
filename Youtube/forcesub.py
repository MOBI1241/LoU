import asyncio
from pyrogram import Client, enums
from Youtube.config import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


########################🎊 Lisa | NT BOTS 🎊######################################################

async def handle_force_subscribe(bot, message):
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(int(Config.CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="מצטער קיבלת באן.",
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="אנא הצטרף לערוץ שלי בשביל להשתמש בבוט!\n\nרק משתמשים שרשומים לערוץ יכולים להשתמש בבוט!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 בבקשה תרשמו לערוץ שלי 🤖", url=invite_link.invite_link)
                    ],
                ]
            ),
            
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Something Went Wrong. Contact My [Support Group](https://t.me/NT_BOTS_SUPPORT).",
            disable_web_page_preview=True,
        )
        return 400

########################🎊 Lisa | NT BOTS 🎊######################################################
