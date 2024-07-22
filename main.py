import logging

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

from YouTubeAPI import search_videos_by_name

TOKEN = "7422836443:AAF2AanhiLNKGHxBiizln5Tqn1pQZpLKvDo"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    search_text = ' '.join(context.args)
    response = search_videos_by_name(request_text=search_text)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Я нашел видео '{response[1]}'\n {response[0]}")


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="К сожалению, данная команда мне не знакома")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    caps_handler = CommandHandler('search', search)
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_command_handler = MessageHandler(filters.COMMAND, unknown_command)


    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_command_handler)

    application.run_polling()
