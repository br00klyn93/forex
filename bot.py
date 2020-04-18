from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from telegram.ext import MessageHandler, Filters

from flask import Flask
from flask import request
from flask_cors import CORS
from datetime import datetime

import requests

app = Flask(__name__)
CORS(app)


updater = Updater(token='1246775743:AAEifr_IQFT7VeSAl9waeyIA2ZoUGYBEOCA', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot Initialized.")

@app.route('/')
def main():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    # update.message.text is how you get any text posted to the channel
    print(update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
