import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    city1 = types.KeyboardButton('Tashkent')
    city2 = types.KeyboardButton('Andijon')
    city3 = types.KeyboardButton('Bukhara')
    city4 = types.KeyboardButton('Fergana')
    city5 = types.KeyboardButton('Jizzakh')
    city6 = types.KeyboardButton('Horazm')
    city7 = types.KeyboardButton('Namangan')
    city8 = types.KeyboardButton('Qashqadaryo')
    city9 = types.KeyboardButton('Samarqand')
    city10 = types.KeyboardButton('Sirdaryo')
    city11 = types.KeyboardButton('Surxondaryo')
    city12 = types.KeyboardButton('Karakalpakstan')

    markup.add(city1,city2,city3,city4,city5,city6,city7,city8,city9,city10,city11,city12)


    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!", reply_markup=markup)



@dp.message_handler()
async def get_weather(message: types.Message):
    if message.text == 'Tashkent':
        tash = open('tashkent.png','rb')
        await message.answer_photo(tash)

    elif message.text == 'Andijon':
        a = open('andijan.png','rb')
        await message.answer_photo(a)

    elif message.text == 'Fergana':
        b = open('fergana.png','rb')
        await message.answer_photo(b)

    elif message.text == 'Jizzakh':
        c = open('jizzakh.png','rb')
        await message.answer_photo(c)

    elif message.text == 'Namangan':
        d = open('namangan.png','rb')
        await message.answer_photo(d)

    elif message.text == 'Horazm':
        e = open('surhandaryo.png','rb')
        await message.answer_photo(e)

    elif message.text == 'Qashqadaryo':
        f = open('qashqadaryo.png','rb')
        await message.answer_photo(f)

    elif message.text == 'Samarqand':
        j = open('samarqand.png','rb')
        await message.answer_photo(j)

    elif message.text == 'Sirdaryo':
        q = open('sirdaryo.png','rb')
        await message.answer_photo(q)

    elif message.text == 'Surxondaryo':
        s = open('surhandaryo.png','rb')
        await message.answer_photo(s)


    elif message.text == 'Karakalpakstan':
        u = open('karakalpakstan.png','rb')
        await message.answer_photo(u)



    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"***Хорошего дня!***"
              )

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)