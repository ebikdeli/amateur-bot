from telegram import Update
from telegram.ext import ContextTypes
import os
import logging


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages"""
    user = update.effective_user.username
    user_message = update.message.text
    await update.message.reply_html(f'"{user}" says "{user_message}"')
    logger.info(f'Echoed message from {user}: {user_message}')


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle help command"""
    msg = """Tutorial to use this bot. Enter the following commands and see what they do:\n\n
"/start" to start a conversation with the bot\n
"/payment" to pay the bill\n
"/products" to see all the products in the store\n"""
    await update.message.reply_html(msg)
    logger.info('Displayed help message')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle start command"""
    user = update.effective_user.username
    msg = f'Welcome to the amateur bot, {user}!\nPlease feel free to use our bot.'
    await update.message.reply_text(msg)
    logger.info(f'Started conversation with {user}')


async def text_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text documents"""
    chat_id = update.effective_chat.id
    file_id = update.message.document.file_id
    try:
        file = await context.bot.get_file(file_id)
        cwd = os.getcwd()
        downloaded_file = await file.download(os.path.join(cwd, 'my_new_text_file.txt'))
        await context.bot.send_document(chat_id, downloaded_file.file_path)
        logger.info(f'Downloaded and sent document for chat_id {chat_id}')
    except Exception as e:
        logger.error(f'Error downloading document: {e}')
        await update.message.reply_text('Sorry, there was an error processing your document.')


async def handle_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle MP3 files"""
    chat_id = update.effective_chat.id
    file_id = update.message.audio.file_id
    try:
        file = await context.bot.get_file(file_id)
        cwd = os.getcwd()
        downloaded_file = await file.download(os.path.join(cwd, 'downloaded_audio.mp3'))
        await update.message.reply_text('MP3 file received and processed.')
        logger.info(f'Downloaded and processed MP3 file for chat_id {chat_id}')
    except Exception as e:
        logger.error(f'Error downloading MP3 file: {e}')
        await update.message.reply_text('Sorry, there was an error processing your MP3 file.')