import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pass2


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    print('Вызван /start')
    logging.info('Вызван /start')
    text = 'Привет, ' + update.message.chat.first_name + ' ' + update.message.chat.last_name
    context.bot.sendMessage(chat_id=update.message.chat_id, text=text)
    print('Пользователю отпавлено сообщение: ', text)
    logging.info('Пользователю отпавлено сообщение: ' + text)


def talk_to_me(update, context):
    text = 'Вы написали нам: ' + update.message.text
    logging.info('Пользователь написал нам: ' + update.message.text)
    print('Пользователь написал нам: ', update.message.text)
    context.bot.sendMessage(chat_id=update.message.chat_id, text=text)
    print('Пользователю отпавлено сообщение: ', text)
    logging.info('Пользователю отпавлено сообщение: ' + text)


def main():
    my_bot = Updater(pass2.token)

    logging.info('Бот запускается')
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()


main()
