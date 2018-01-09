# -*- coding: utf-8 -*-

import telebot
from fence import fence
from reverse import reverse
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, 'This bot will corrupt your text. Inline mode supported.')


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "Just type bot's nickname and text in chat.")


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def corrupt_text(query):
    try:
        fence_result = fence(query.query)
        reverse_result = reverse(query.query)
        r1 = telebot.types.InlineQueryResultArticle('1', fence_result, telebot.types.InputTextMessageContent(fence_result))
        r2 = telebot.types.InlineQueryResultArticle('2', reverse_result, telebot.types.InputTextMessageContent(reverse_result))
        bot.answer_inline_query(query.id, [r1, r2])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop=True)
