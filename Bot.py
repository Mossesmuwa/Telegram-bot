#!/usr/bin/env python3
import os
from datetime import datetime
from telethon import TelegramClient, events
from cryptography.fernet import Fernet

# ----------------------------
# CONFIGURATION
# ----------------------------
api_id = 123456            # Replace with your API ID
api_hash = "your_api_hash" # Replace with your API hash
bot_token = "your_bot_token" # Bot token from BotFather
download_folder = "downloads"
encrypt_files = True        # Toggle encryption ON/OFF

# Encryption key (generate once and save securely!)
encryption_key = Fernet.generate_key()
fernet = Fernet(encryption_key)

# ----------------------------
# SETUP
# ----------------------------
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

bot = TelegramClient("filebot", api_id, api_hash).start(bot_token=bot_token)

# ----------------------------
# HELPER FUNCTION
# ----------------------------
def save_file(file_path: str, encrypt: bool = False) -> str:
    if encrypt:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted_data)
    return file_path

# ----------------------------
# EVENT HANDLER
# ----------------------------
@bot.on(events.NewMessage)
async def handler(event):
    if event.message.file:
        original_name = event.message.file.name or "file"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{timestamp}_{original_name}"
        path = os.path.join(download_folder, new_name)
        
        await event.message.download_media(file=path)
        saved_path = save_file(path, encrypt=encrypt_files)
        
        await event.reply(
            f"✅ File saved as `{new_name}`\n"
            f"🔒 Encrypted: {'Yes' if encrypt_files else 'No'}"
        )

print("🚀 Telegram File Bot running...")
bot.run_until_disconnected()
