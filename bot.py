import telebot
import logging
from config import BOT_TOKEN, ADMIN_ID, TARGET_GROUP_ID, SOURCE_GROUP_ID
from bot_handlers import BotHandlers

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Import config as object
class Config:
    TELEGRAM_BOT_TOKEN = BOT_TOKEN
    ADMIN_ID = ADMIN_ID
    TARGET_GROUP_ID = TARGET_GROUP_ID
    SOURCE_GROUP_ID = SOURCE_GROUP_ID

config = Config()

# Initialize handlers
handlers = BotHandlers(bot, config)
handlers.register_handlers()

logger.info("TeleHelper Bot started successfully!")

if __name__ == '__main__':
    try:
        logger.info("Bot polling started...")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"Bot polling error: {e}")