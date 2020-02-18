import telebot
import config
import MyPars


bot = telebot.TeleBot(config.token)
chat_id = ''


@bot.message_handler(commands=['help'])
def message2(message):
    bot.send_message(message.chat.id, 'Ты написал Help',  reply_markup = keyboard())


@bot.message_handler(content_types=['text'])
def message1(message):
    weather = []
    if message.text == 'Погода':
        weather = MyPars.my_parse()
        bot.send_message(message.chat.id, weather[4])


def keyboard():
    mark = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Погода')
    mark.add(btn1)
    return mark


bot.polling(none_stop=True)



