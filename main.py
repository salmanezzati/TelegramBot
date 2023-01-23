import telebot7

token = '5978617267:AAHK6YtgNOVjWvre2HZdLLYh54sgw0lzMpc'
bot = telebot7.TeleBot(token)

@bot.message_handler(commands=['start', 'help', 'hello'])
def sendWelcome(message):
    print(message.text)
    bot.reply_to(message, 'Hi im Sam. what can i do for you?')

@bot.message_handler(func=lambda m:True)
def echoAll(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

