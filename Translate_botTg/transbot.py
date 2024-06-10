import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
from os import environ

# Встановлення логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Введіть свій токен, отриманий від BotFather
TOKEN = environ.get("TRANSLATE_BOT_TOKEN","define me")

# Ініціалізація перекладача
translator = Translator()

# Функція старту
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Я бот для перекладу тексту. Відправ мені текст, і я перекладу його на англійську.')

# Функція допомоги
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Відправ мені текст, і я перекладу його на англійську.')

# Функція обробки текстових повідомлень
def translate_text(update: Update, context: CallbackContext) -> None:
    text_to_translate = update.message.text
    translated = translator.translate(text_to_translate, dest='en')
    update.message.reply_text(translated.text)

def main() -> None:
    # Введіть свій токен тут

    updater = Updater(TOKEN)
    
    logger.info("News bot Started")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
