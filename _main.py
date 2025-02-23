import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import dotenv_values


# Import telegram bot token
dotenv_vars = dotenv_values('.env')
BOT_TOKEN = dotenv_vars.get('BOT_TOKEN', None)
if not BOT_TOKEN:
    input('There is no "BOT_TOKEN". Enter any key to exit...')
    exit()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


application = Application.builder().token(BOT_TOKEN).build()


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages"""
    user = update.effective_user.username
    user_message = update.message.text
    await update.message.reply_html(f'"{user}" says "{user_message}"')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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


application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

application.add_handler(CommandHandler('help', help))

application.add_handler(CommandHandler('start', start))

application.run_polling(allowed_updates=Update.ALL_TYPES)
