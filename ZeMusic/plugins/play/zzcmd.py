import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZeMusic import app
from ZeMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
import config                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b> -› مرحبا بك </b> .\n\n<b>-› جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت \nواستكشف ياوحش </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اوامر التشغيل ", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        " اوامر القناة ", callback_data="zzzch"),
                    InlineKeyboardButton(
                        " اوامر الادمن ", callback_data="zzzad"),
                
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b> مرحباً بك عـزيزي المطور </b>\n\n<b> -› استخدم الازرار بالاسفل \n -›واستكشف اوامر الميوزك </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " التحديث ", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        " الـرفع ", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        " الحظر ", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        " الاشعارات & المساعد ", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
 <b>قائمة اوامر التشغـيل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- لتشـغيل اغنية في المكالمة الصونية</b>

بحث + الاسـم
<b>- لتحميل الاغاغي والمقاطـع الصوتيه من اليوتيوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
 <b>قائمة اوامر الادمن :</b>


الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / اسكت
<b>- لإيقاف تشغيل الموسيقى في المكالمه</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي / التالي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

/الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>

رفع ادمن/تنزيل ادمن
<b>- لـ رفـع/تنزيـل ادمـن فـي البـوت</b>

الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
/seekback + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل المكالمه</b>
<b>- انشاء مجموعه وارفع البوت اشراف</b>
<b>- ارسـل في المجموعه (/channelplay او /ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل بالمجموعه لـ التشغيـل</b>
<b>- "استخدم الاوامر بـ / او بدون"</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
cplay + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

cvplay + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

cstop
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

cpause
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

cresume
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

cskip
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

/السجلات
<b>- لـ جلب سجـلات البـوت 📋</b>

/تحديث
<b>- لـ تحديـث البــوت</b>

/اعاده تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

حظر/الغاء الحظر
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>

المحظورين
<b>- لـ عـرض قائمـة المحظورين</b>

حظر عام/الغاء حظر عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>

مغادره تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
   )
