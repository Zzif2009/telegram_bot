from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler

TOKEN = "1125754673:AAEOZqphw96-AK2SWfaS1ObQVG7S-OjP70g"


def echo(update, context):
    update.message.replay_text(update.message.text)


def start(update, context):
    update.message.replay_text("Hello, world!")


def help(update, context):
    update.message.replay_text("I can`t do it.")


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
