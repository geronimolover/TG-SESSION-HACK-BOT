api_id = os.environ.get("API_ID") 
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")


client = TelegramClient('TeamIndia', api_id, api_hash).start(bot_token=token)
