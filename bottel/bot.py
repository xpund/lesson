from telegram.ext import Updater
import pass2


def main():
    mybot = Updater(pass2.token)
    mybot.start_polling()
    mybot.idle()

    print(mybot.logger)


main()
