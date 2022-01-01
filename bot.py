from pyrogram import filters, Client
from pyrogram.types import ( ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from time import sleep
from pyrogram.types.messages_and_media import message
app = Client(
    "bot",
    api_id=1712043,
    api_hash="965c994b615e2644670ea106fd31daaf",
    bot_token="5073878916:AAGhW3Mw66WUgEwAFdMLyLYOezys2gQmUgg"
)

@app.on_message(filters.command('start'))
def command(app,message):
    # app.send_message(message.chat.id, "hello brother\n **THis bot is not completed yet**\t\n **this bot is for testing only** \n\towner is @mrwolverine_genuine")
    app.send_message ( message.chat.id, "**Hello Guys\n Please join our channel\n\t Look at that button!**\n 👇",reply_markup=InlineKeyboardMarkup([
   [InlineKeyboardButton("channel", url="https://t.me/campus_diaries_download")]
    ]))
    # app.send_message(message.chat.id, "**Look at that button!**\n 👇",reply_markup=ReplyKeyboardMarkup([["Noice","nudes idher bheje"]]))
   



print("i AM alive sur")
app.run()
 
