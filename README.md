# TeleHelper Bot 🤖

A powerful Telegram bot for intelligent group member management and automation.

## Features ✨

- ✅ **Member Management** - Add, remove, and list group members
- ✅ **Admin Controls** - Restricted commands for authorized users only
- ✅ **Easy Setup** - Simple configuration with .env file
- ✅ **Logging** - Track all bot activities
- ✅ **Error Handling** - Robust error management
- ✅ **User-Friendly** - Simple commands and clear responses

## Requirements 📋

- Python 3.8+
- pip (Python package manager)
- Telegram Bot Token (from BotFather)

## Installation 🚀

### 1. Clone the repository
```bash
git clone https://github.com/Vinayakkhandal/Telehelper.git
cd Telehelper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your Telegram Bot Token
1. Open Telegram and search for **@BotFather**
2. Send `/start` and follow the prompts
3. Use `/newbot` to create a new bot
4. Copy your bot token

### 4. Get your User ID
1. Search for **@userinfobot** on Telegram
2. Send `/start` to get your user ID

### 5. Setup .env file
```bash
cp .env.example .env
```

Edit `.env` and fill in:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_user_id_here
TARGET_GROUP_ID=your_target_group_id
SOURCE_GROUP_ID=your_source_group_id
```

### 6. Run the bot
```bash
python bot.py
```

## Available Commands 📞

| Command | Description | Admin Only |
|---------|-------------|-----------|
| `/start` | Start the bot | No |
| `/help` | Show help message | No |
| `/add_members` | Add members from source group | Yes |
| `/list_members` | List all members | Yes |
| `/remove_member` | Remove a member | Yes |

## How to Get Group IDs 🔍

1. Add bot to your group
2. Send a message in the group
3. Send `/list_members` command
4. The group ID will be displayed

## Project Structure 📁

```
Telehelper/
├── bot.py              # Main bot file
├── config.py           # Configuration file
├── bot_handlers.py     # Command handlers
├── requirements.txt    # Dependencies
├── .env.example        # Example environment file
└── README.md           # This file
```

## Deployment 🌐

### Using Heroku (Free)
```bash
# Create Procfile
echo "worker: python bot.py" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
heroku config:set TELEGRAM_BOT_TOKEN=your_token
```

### Using Cloud Server (AWS, DigitalOcean, etc.)
1. SSH into your server
2. Clone the repository
3. Install Python and dependencies
4. Use `screen` or `nohup` to run the bot
5. Or use `systemd` for auto-restart

## Troubleshooting 🔧

**Bot not responding?**
- Check if bot token is correct
- Ensure bot is added to the group as admin
- Check logs for errors

**Permission denied errors?**
- Make sure you're using correct Admin ID
- Verify group IDs are correct

**ModuleNotFoundError?**
- Run `pip install -r requirements.txt` again
- Check Python version (3.8+)

## Contributing 🤝

Feel free to fork and submit pull requests!

## License 📜

MIT License - Feel free to use this project

## Support 💬

For issues or questions, open a GitHub issue or contact the maintainer.

---

**Made with ❤️ by Vinayakkhandal**