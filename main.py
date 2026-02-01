import telebot

API_TOKEN = '8234630254:AAEtzUPEAusot_e8T0FXzCC6JMsb4iNrlVg'
ADMIN_ID = 8014746288
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome! I am your Telegram bot.')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.remove_webhook()  # Remove any existing webhooks
    bot.set_webhook(url='https://your-render-url/webhook')  # Add your Render URL here
    print('Webhook set!')
    bot.polling(none_stop=True)