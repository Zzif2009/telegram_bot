from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "1105077082:AAEAn3qLd5SKtJOow0-azH0S9qR53K6DI9c"
reply_keyboard = [
    [
        "/address", "/phone"
    ],
    [
        "/site", "work_time"
    ]
]
MARKUP = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def echo(update, context):
    update.message.replay_text(update.message.text)


def start(update, context):
    update.message.replay_text("Hello, world!", reply_markup=reply_keyboard)


def help(update, context):
    update.message.replay_text("I can`t do it.")


def address(update, context):
    update.message.replay_text("Address")


def phone(update, context):
    update.message.replay_text("+79040520738")


def site(update, context):
    update.message.replay_text("https://vk.com")


def work_time(update, context):
    update.message.replay_text("from 8:00 until 17:00")


def close_keyboard(update, context):
    update.message.replay_text("OK", reply_markup=ReplyKeyboardRemove())


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("close_keyboard", close_keyboard))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
