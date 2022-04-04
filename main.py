import telebot #pyTelegramBotAPI

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(func=lambda m: True)
def do_repeat(message):
 bot.send_message(message.chat.id, message.text)

if name == '__main__':
 bot.infinity_polling()
