# 📁 Telegram File Bot

A Python bot that automatically downloads files sent to it via Telegram, renames them with a timestamp, and optionally encrypts them using **Fernet (AES)**.

---

## ✨ Features
- Receives files (images, videos, documents, etc.) via Telegram.
- Automatically renames files with a timestamp prefix.
- Optional encryption using Fernet.
- Sends a confirmation message back to the user.
- Compatible with Linux, Windows, and Termux.

---

## 📂 Project Structure

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/telegram-file-bot.git
cd telegram-file-bot
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    encryption_key = f.read()
fernet = Fernet(encryption_key)


