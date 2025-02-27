from telegram import Update
from telegram.ext import ContextTypes
import os


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages"""
    user = update.effective_user.username
    user_message = update.message.text
    await update.message.reply_html(f'"{user}" says "{user_message}"')


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle help command"""
    msg = """Toturial to use this bot. Enter following commands and the thing they do:\n\n
"/start" to start conversation with the bot\n
"/payment" to pay the bill\n
"/products" to see all the products in the storel\n"""
    await update.message.reply_html(f'{msg}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle start command"""
    user = update.effective_user.username
    msg = f'Welcome to the amateur bot {user}\nPlease fill free to use our bot'
    await update.message.reply_text(f'{msg}')


async def text_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text documents"""
    chat_id = update.effective_chat.id
    file_id = update.message.document.file_id
    file = await context.bot.get_file(file_id)
    cwd = os.getcwd()
    downloaded_file = await file.download_to_drive(os.path.join(cwd, 'my_new_text_file.txt'))
    await context.bot.send_document(chat_id, str(downloaded_file))
