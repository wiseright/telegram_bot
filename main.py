import os
import telebot
from dotenv import load_dotenv
import requests

# The function return the rate exchange
def get_rate(rate_token_url, currency):
    # Get token from: https://www.exchangerate-api.com/docs/python-currency-api
    # rate_token_url should be: https://v6.exchangerate-api.com/v6/8e0f6d6cb8cc05f3d47f0e00/latest/USD
    response = requests.get(rate_token_url)
    data = response.json()

    return data['conversion_rates'][currency]

# this function answer to the user, after him/her asked for /change command
def currency_handler(message):
    sign = message.text
    text = f"Today the change is: {get_rate(RATE_TOKEN, sign)}"
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")



load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
RATE_TOKEN = os.getenv('RATE_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Ciao, bella Saetta?")

# this handler manage the change rate answer
@bot.message_handler(commands=['change'])
def sign_handler(message):
    text = "What's your currency?\nChoose one: *EUR*, *USD*, *AED*, *AFN*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, currency_handler)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()


