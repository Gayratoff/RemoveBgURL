
from time import sleep
import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart

TOKEN = "5058492849:AAFc0KMwvKpkOf-Fz56cEbedzw4aMsw0TYo"
BG_TOKEN="ESM9SKqwiQCNUDfVedVKJnYL" # API KEY JOYLASH JOYI
bot =Bot(token=TOKEN)
dp =Dispatcher(bot)

# removebg saytidan API KEY OLASIZLAR...
# ADMIN @MISTRUZ
# VIP KANAL UCHUN MAXSUS
#SOTILMASIN VA TARQALMASIN TAQIQLANADI

@dp.message_handler(CommandStart())
async def start_bot(message : types.Message):
    await message.reply(f"<b>Salom {message.from_user.first_name} ! \nBu bot orqali rasmlarni PNG holatga keltirishingiz mumkin </b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=['photo'])
async def echo_message(message: types.Message):
    msg = await message.answer("Yuklanmoqda...⏳")
    sleep(0.2)
    await msg.edit_text("Yuklanmoqda.⌛️")
    sleep(0.3)
    await msg.edit_text("Yuklanmoqda..⏳")
    sleep(0.4)
    await msg.edit_text("Yuklanmoqda...🚀")
    sleep(0.2)
    await msg.edit_text("Yuklandi...🚀")
    sleep(0.5)
    await msg.delete()
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    print(photo_url)
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': photo_url,
            'size': 'auto'
        },
        headers={'X-Api-Key': BG_TOKEN},
    )
    if response.status_code == requests.codes.ok:
        with open(f'photos/on{message.chat.id}-bg.png', 'wb') as out:
            out.write(response.content)
            name_bot = await bot.get_me()
            await bot.send_photo(chat_id=message.from_user.id,photo=open(f'photos/on{message.chat.id}-bg.png', 'rb'),caption=f"@{name_bot.username} Orqali Tayorlandi")
            await bot.send_document(chat_id=message.from_user.id,document=open(f'photos/on{message.chat.id}-bg.png', 'rb'),caption=f"@{name_bot.username} Orqali Tayorlandi")
    else:
        print("Error:", response.status_code, response.text)

# removebg saytidan API KEY OLASIZLAR...
# ADMIN @MISTRUZ
# VIP KANAL UCHUN MAXSUS
#SOTILMASIN VA TARQALMASIN TAQIQLANADI


if __name__ == '__main__':
    executor.start_polling(dp)

