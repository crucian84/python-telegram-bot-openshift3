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
    """Вывести сообщение, когда отправлена команда /start.
    Обычно это приветственное сообщение"""
    """update.message.reply_text('Welcome to the Test Bot! I will reply you what you will write me.')"""
    bot.send_message(chat_id=update.message.chat_id,
                     text='<b>KAZGUU site</b>,<a href="http://kazguu.kz/ru/">KAZGUU</a>', parse_mode=ParseMode.HTML)


def help(bot, update):
    """Вывести сообщение, когда отправлена команда /start.
    Это может быть сообщение о том, что ваш бот может делать и список команд"""
    update.message.reply_text('Тут вы можете получить любую помощь.')

    keyboardButtons = [[InlineKeyboardButton("Помощь", callback_data="1")],
                       [InlineKeyboardButton("Примеры", callback_data="2")],
                       [InlineKeyboardButton("Ссылка", url="http://google.com")]]
    keyboard = InlineKeyboardMarkup(keyboardButtons)
    update.message.reply_text('Сделайте выбор:', reply_markup=keyboard)


def button(bot, update):
    query = update.callback_query
    if query.data == "1":
        text = "Вы можете использовать какое-либо из данных действий: +, -, /, *"
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

def convert(bot, update, args):
    try:
        #dollars = int(update.message.text)
        dollars = args
        tenge = dollars * 373
    except (NameError, SyntaxError, ValueError):
        tenge = "Введите целое число"
    bot.send_message(chat_id=update.message.chat_id, text=tenge)


#def echo(bot, update):
#    update.message.reply_text('Вы ввели:  ' + update.message.text)


def error(bot, update, error):
    """Запись всех ошибок вызванных Updates."""
    logger.warning('Update "%s" caused error "%s"' % (update, error))



def main():
    """If webhook_url is not passed, run with long-polling.
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:"""
    updater = Updater(TOKEN)  # Создаем EventHandler (обработчик событий) и передаем ему токен (ключ) бота.
    #bot = updater.bot
    dp = updater.dispatcher  # Объявление диспетчера, чтобы потом зарегистрировать handlers (обработчики)
    dp.add_handler(CommandHandler("start", start))  # Отвечает на команду /start в Телеграм
    dp.add_handler(CommandHandler("help", help))  # Отвечает на команду /help в Телеграм
    dp.add_handler(CommandHandler("convert", convert, pass_args=True))
    dp.add_handler(CallbackQueryHandler(button))

    # Для ответа бота на текстовые (не командные) сообщения.
    #dp.add_handler(MessageHandler(Filters.text, echo))  # Бот отвечает тем сообщением, которое вы ему написали (эхо-бот)
    # dp.add_handler(MessageHandler(Filters.text, guessing))

    # Запись всех ошибок
    dp.add_error_handler(error)

    """if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook"""
    updater.start_polling()  # Start the Bot
    """Бот будет работать до тех пор пока вы не нажмете Ctrl-C
     или процесс не получит SIGINT, SIGTERM или SIGABRT. 
     Этот способ должен использоваться в большинстве случаев т.к. start_polling()
      не блокирующий и остановит бота правильно."""
    updater.idle()


if __name__ == '__main__':
    main()
