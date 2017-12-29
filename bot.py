# -*- coding: utf-8 -*-

import telebot
import fence
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def msg(message):
    result = fence.fence(message.text)
    bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    bot.polling(none_stop=True)
