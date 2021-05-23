"""
This is my first bot and it's a test bot
    for now it will send you animal pictures :)

Deployed using Heroku.
Author: Maripillon
Bot: maripillon_test_bot
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = "1655535403:AAGQE-7RsL4b-6CNksadgVsSFJzXqfPDcd0"


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    text = """Now we can talk :)
            How are you?"""
    update.message.reply_text(text)


# def send_animal_pic(update, context):
#     """Send animal pictures. """
#     context.bot.sendPhoto(chat_id=update.message.chat_id,
#                         photo='https://s.abcnews.com/images/Lifestyle/gty_baby_pandas_02_jc_160930_16x9_992.jpg')


def help(update, context):
    """Send a message when the command /help is issued."""
    text = """Hi! I'm the Blue Kiwi.
            I'm not that complicated :)
            just start talking to me :]"""
    update.message.reply_text(text)


def echo(update, context):
    """Echo the user message. """
    print(update.message.text)
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - process user's sentence
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot

    # Using Local
    # updater.start_polling()

    # Using Heroku
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://afternoon-woodland-88766.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
