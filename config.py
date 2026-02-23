import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', '0'))
TARGET_GROUP_ID = int(os.getenv('TARGET_GROUP_ID', '0'))
SOURCE_GROUP_ID = int(os.getenv('SOURCE_GROUP_ID', '0'))

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in .env file")