import logging
import random
#from queue import Queue
#from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '693266929:AAHv5cYEQmTI0kkClSWNK-CtRr7oqrXp3mI'


def start(bot, update):
    """Send a message when the command /start is issued."""
    """update.message.reply_text('Welcome to the Test Bot! I will reply you what you will write me.')"""
    bot.send_message(chat_id=update.message.chat_id,
                     text='<b>KAZGUU site</b>,<a href="http://kazguu.kz/ru/">KAZGUU</a>', parse_mode=ParseMode.HTML)


def help(bot, update):
    """Send a message when the command /help is issued."""
    # update.message.reply_text('You can get any help here.')

    keyboardButtons = [[InlineKeyboardButton("Помощь", callback_data="1")],
                       [InlineKeyboardButton("Примеры", callback_data="2")],
                       [InlineKeyboardButton("Ссылка", url="http://google.com")]]
    keyboard = InlineKeyboardMarkup(keyboardButtons)
    update.message.reply_text('Сделайте выбор:', reply_markup=keyboard)


def button(bot, update):
    query = update.callback_query
    if query.data == "1":
        text = "You can choose any of the following actions: +, -, /, *"
    elif query.data == "2":
        text = "3+4, 44-12, 43/2, 12*90"
    bot.editMessageText(text=text, chat_id=query.message.chat_id,
                        message_id=query.message.message_id)


"""class arr:

    def __init__(self, num, random_num=random.randint(1, 100)):
        self.random_num = random_num
        self.num = num

    def checking(self, bot, update):
        try:
            if self.random_num == self.num:
                ar = 'Вы выиграли!'
            elif self.random_num > self.num:
                ar = 'Ваше число меньше моего. Попробуйте еще раз :)'
            elif self.random_num < self.num:
                ar = 'Ваше число больше моего. Попробуйте еще раз :)'
            # ar = int(num) * 370
        except (NameError, SyntaxError, ValueError):
            ar = "Введите целое число"
        bot.send_message(chat_id=update.message.chat_id, text=ar)


def guessing(bot, update):
    input_num = int(update.message.text)
    object_num = arr()
    object_num.checking(input_num)
"""

"""def echo(bot, update):
    update.message.reply_text('You said:  ' + update.message.text)
"""

def dolintenge(bot, update, args):
    dollars = int(args)
    tenge = dollars * 356
    update.message.reply_text(text=tenge)



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"' % (update, error))



def main():
    """If webhook_url is not passed, run with long-polling.
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:"""
    updater = Updater(TOKEN)  # Create the EventHandler and pass it your bot's token.
    bot = updater.bot
    dp = updater.dispatcher  # Get the dispatcher to register handlers
    dp.add_handler(CommandHandler("start", start))  # on /start command answer in Telegram
    dp.add_handler(CommandHandler("help", help))  # on /help command answer in Telegram
    dp.add_handler(CommandHandler("dolintenge", dolintenge))
    dp.add_handler(CallbackQueryHandler(button))

    # on noncommand i.e message - echo the message on Telegram
    """dp.add_handler(MessageHandler(Filters.text, echo))"""
    # dp.add_handler(MessageHandler(Filters.text, guessing))

    # log all errors
    dp.add_error_handler(error)

    """if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:"""
    bot.set_webhook()  # Delete webhook
    updater.start_polling()  # Start the Bot
    """Run the bot until you press Ctrl-C or the process receives SIGINT,
    SIGTERM or SIGABRT. This should be used most of the time, since
    start_polling() is non-blocking and will stop the bot gracefully."""
    updater.idle()


if __name__ == '__main__':
    main()
