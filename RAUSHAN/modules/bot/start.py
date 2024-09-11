from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    " ✦𝐇ᴇʏ..! 𝐌ᴀsᴛᴇʀ..!!👋!\n\n✦ 𝐈'ᴍ A 𝐏ᴏᴡᴇʀғᴜʟ 𝐌ɪᴛᴢᴀ's Iᴅ 𝐔sᴇʀʙᴏᴛ 𝐇ᴇʟᴘᴇʀ?\n\n‣ I Cᴀɴ Hᴇʟᴘ Yᴏᴜ Tᴏ Hᴏsᴛ Yᴏᴜʀ Lᴇғᴛ Cʟɪᴇɴᴛs. \n\n‣ Tʜɪs Is Sᴘᴇᴄɪᴀʟʟʏ Fᴏʀ Cʜᴀᴛ Fʏᴛᴇʀs\n\n‣ Nᴏᴡ /clone {send your PyroGram ᴠ2 String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⚡Oᴡɴᴇʀ 💕⚡", url="t.me/FuckTheSn1tches"),
            ],
            [
                InlineKeyboardButton("⚡Cʜᴀɴɴᴇʟ 💕⚡", url="https://t.me/userbot_channel_tnw"),
            ],
            [
                InlineKeyboardButton("⚡Sᴜᴘᴘᴏʀᴛ 💕⚡", url="https://t.me/+qYRBJgZsARpkNWJl"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐓𝐖𝐎 𝐌𝐈𝐍𝐔𝐓𝐄𝐒...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="RAUSHAN/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 𝐓𝐍𝐖 𝐂𝐄𝐎 𝐌𝐈𝐓𝐙𝐀 𝐇𝐄𝐑𝐄 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
