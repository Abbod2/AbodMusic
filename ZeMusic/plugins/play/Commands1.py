import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from ZeMusic import Mody
from ZeMusic.utils.decorators.admins import AdminActual
from ZeMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from ZeMusic import Telegram, YouTube, app
from ZeMusic.misc import SUDOERS
from ZeMusic.plugins.play.playlist import del_plist_msg
from ZeMusic.plugins.sudo.sudoers import sudoers_list
from ZeMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from ZeMusic.utils.decorators.language import LanguageStart
from ZeMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from ZeMusic import check_client


@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n╭── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/NvvvC) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **ميرا شغلي + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **ميرا طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ميرا الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ميرا اص** او **اسكتي**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ميرا تكلمي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ميرا ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ميرا كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/NvvvC) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/so_alfaa")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴍɪʀᴀ", callback_data="fft"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("sop"))
async def sop(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂\n✧ 𝑱𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑴𝒊𝒓𝒂 𝑻𝒐 𝑺𝒆𝒆 𝑨𝒍𝒍 𝑼𝒑𝒅𝒂𝒕𝒆\n\n- 𝑴𝒂𝒔𝒕𝒆𝒓 -› @C_C_1\n- 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 -› @NvvvC""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/so_alfaa")
                ],[
                    InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴍɪʀᴀ◌", callback_data="am"),
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/c_c_1")
                ],[

                    InlineKeyboardButton(
                        "رجوع", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )
