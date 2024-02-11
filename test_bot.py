import os
import telebot
# from database import Database
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    user = message.from_user
    # query = f"""INSERT INTO customers (first_name) VALUES ('{user.first_name}')"""
    # print(f"{user.first_name} save database {Database.connect(query)}")
    print(f"starting {user.first_name}")
    bot.reply_to(message, f"Salom {user.first_name}, nima gap birodar")

@bot.message_handler(func=lambda msg: True)
def send_welcome(message):
    user = message.from_user
    print(f"starting {user.first_name}")
    bot.reply_to(message, f"bu bot hali toliq emas")
#
# @bot.message_handler(func=lambda msg: True)
# def send_welcome1(message):
#     user = message.from_user
#     print(f"starting {user.first_name}")
#     bot.reply_to(message, f"kel sen bilan bir oyin oynaymiz")
#
# @bot.message_handler(func=lambda msg: True)
# def send_welcome2(message):
#     user = message.from_user
#     print(message.from_user)
#     bot.reply_to(message, f"rozimisan")
#
# @bot.message_handler(func=lambda msg: True)
# def send_welcome3(message):
#     user = message.from_user
#     print(message.from_user)
#     bot.reply_to(message, f"unda boshladik")
#
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     user = message.from_user
#     print(message.first_user)
#     bot.reply_to(message, f"{user.first_name},"f"Sumalak qilelu?")

if __name__ == "__main__":
    bot.infinity_polling()
