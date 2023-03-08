import time
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

TOKEN=os.getenv("TOKEN")

logging.basicConfig(level = logging.INFO) #нужно логирование в файл!
bot = Bot(token=TOKEN)
dp = Dispatcher(bot = bot)

def transliterate(surname):
    translit_dict = {'а': 'a','б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e','ё': 'e','ж': 'zh','з': 'z','и': 'i', 'й': 'i',
                     'к': 'k','л': 'l','м': 'm','н': 'n', 'о': 'o',
                     'п': 'p','р': 'r','с': 's','т': 't','у': 'u','ф': 'f','х': 'kh','ц': 'ts','ч': 'ch',
                     'ш': 'sh','щ': 'shch','ы': 'y','ъ': 'ie','ь': 'ie','э': 'e','ю': 'iu','я': 'ia'}
    for key in translit_dict:
        surname = surname.lower().replace (key, translit_dict[key])
    return surname.title()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'''Привет, {user_name}!
    Пришли свои ФИО для транслитерации.
    Например, Иванов Иван Иванович'''
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)
    

@dp.message_handler(content_types=['text'])
async def send_translit(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f"{user_name=} {user_id=} sent message: {transliterate(message.text)}")
    await bot.send_message(user_id, transliterate(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)
