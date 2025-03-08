import handlers
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

# Message handlers must have very specific filters
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.echo))
# application.add_handler(MessageHandler(filters.Document.TEXT, handlers.text_doc))
application.add_handler(MessageHandler(filters.Document.ALL, handlers.text_doc))
application.add_handler(MessageHandler(filters.AUDIO, handlers.handle_mp3))

application.add_handler(CommandHandler(['help', 'tutorial'], handlers.help_handler))
application.add_handler(CommandHandler('start', handlers.start))


application.run_polling(allowed_updates=Update.ALL_TYPES)
