import telebot
from decouple import config
from bot.commands import setup_commands
import requests

API_KEY = config("API_KEY")
bot = telebot.TeleBot(API_KEY)

setup_commands(bot)

if __name__ == "__main__":
    bot.infinity_polling()