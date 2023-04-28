# ©  - MetaVoid (Moezilla) And Alexa Team For Modification
# Give Credit ❣️Day

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from os import getenv
import re
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", None)
MONGO_URL = getenv("MONGO_URL", None)

client = Client(SESSION_NAME, API_ID, API_HASH)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in client.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    alexaai = await message.reply("🤭🤏✌️")
    await asyncio.sleep(1)
    await alexaai.edit("**ʙᴏʜᴀᴛ ᴛᴀɪᴊ ʜᴏ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ**")
    await asyncio.sleep(1)
    await alexaai.edit("**ɪ ᴀᴍ ᴅᴏɪɴɢ ᴍʏ ʟᴏᴠᴇ 💕**")
    await alexaai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgEAAxkDAAIDgmRK_iO3cjBds78S1ovoudxOSpWyAAJNAwAC2TepRb-pfUIJA2l2LwQ")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6c6063cc118dc220d656a.png",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ
ᴏғ ♻️ ᴅx ʟᴜᴄᴋy 🔥
━━━━━━━━━━━━━━━━━
ᴅᴀᴛᴀʙᴀsᴇ ʙᴀᴄᴋᴇɴᴅ ʙᴏᴛ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴇʀ [⚡ ᴅx ʟᴜᴄᴋy ⚡](https://t.me/DX_LUCKY_143)
┣★ ʜᴇᴀʀᴛ ᴜs  [❤️ ꜱʜᴀyʀɪ ❤️](https://t.me/shayri_hit)
┣★ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs [all ʙᴏᴛs](https://t.me/DX_info)
┣★ ʟᴜᴄᴋy ɢʀᴏᴜᴩ [💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143)
┣★ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/LUCKY-KING-ROBOT/ID-CHATBOT)
┣★ ɴᴇᴛᴡᴏʀᴋ [🦋ᴅx ɴᴀᴛᴡᴀᴋ🦋](https://t.me/DX_info143)
┗━━━━━━━━━━━━━━━━━┛
💞
ɪꜰ ʜᴀᴠᴇ ᴀɴy qᴜᴇꜱᴛɪᴏɴ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ» ᴛᴏ » ᴍy » [🌹 ᴅx ʟᴜᴄᴋy 🌹] @DX_LUCKY_143""",
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**ᴅx ʟᴜᴄᴋy ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")

@client.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                ""
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:
        alexa.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs [💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143) ᴅɪsᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}")
    if is_alexa:
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs [💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143) ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ")
    

@client.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ"
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:           
        await message.reply_text(f"ᴅx ʟᴜᴄᴋy [💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143)/n ᴄʜᴀᴛʙɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ")
    if is_alexa:
        alexa.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs [💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143) ᴇɴᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}")
    

@client.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴇᴀɢᴇ:[💘 ɢʀᴏᴜᴩ 💘](https://t.me/DXinfo143)**\n/chatbot [on|off] ᴏɴʟʏ ɢʀᴏᴜᴘ")

    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
