#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import os
import sys

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# https://api.telegram.org/bot1415033851:AAFZOnwhaJMsC35zryNxatwP14DBGfAU6WY/getUpdates

# https://api.telegram.org/bot1415033851:AAFZOnwhaJMsC35zryNxatwP14DBGfAU6WY/sendMessage?chat_id=1451035706&text=meow

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context) -> int:
	user = update.message.from_user
	update.message.reply_text('Hi ' + user.first_name + '!! please click /help for more info ' + "\n with ID:" + str(user.id) + "\n \n and Date:" + str(update.message.date) + "\n logger Name:" + logger.name + '\n Update1 "%s" caused error "%s"')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
	user = update.message.from_user
	"""Echo the user message."""
	update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	# updater = Updater("TOKEN", use_context=True)

	updater = Updater("1415033851:AAFZOnwhaJMsC35zryNxatwP14DBGfAU6WY", use_context=True)


	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.



	os.environ.setdefault('DJANGO_SETTINGS_MODULE', "root.settings.dev")
	from django.core.management import execute_from_command_line
#	try:
#		from django.core.management import execute_from_command_line
#	except ImportError as exc:
#		raise ImportError(
#			"Couldn't import Django. Are you sure it's installed and "
#			"available on your PYTHONPATH environment variable? Did you "
#			"forget to activate a virtual environment?"
#		) from exc
	execute_from_command_line(sys.argv)
	updater.idle()


if __name__ == '__main__':
	main()
#	start()
