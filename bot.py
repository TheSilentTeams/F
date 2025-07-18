
import logging
import sys
import logging.config
import asyncio
import os
import time
import requests
from flask import Flask, request
from threading import Thread
from aiohttp import ClientSession
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from apscheduler.schedulers.background import BackgroundScheduler
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, PORT
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script
from plugins import web_server
from aiohttp import web
from datetime import date, datetime 
import pytz
import shutil


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logging.info(f"🔧 Python Version: {sys.version}")

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        logging.info(script.LOGO)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, current_time))

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(self, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                yield message
                current += 1

# Define the bot instance at the top to prevent NameError
app = Bot()

# ===============[ RENDER PORT UPTIME ISSUE FIXED ]================ #

def ping_self():
    url = "https://newauto-15.onrender.com/alive"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("Ping successful!")
        else:
            logging.error(f"Ping failed with status code {response.status_code}")
    except Exception as e:
        logging.error(f"Ping failed with exception: {e}")

flask_app = Flask(__name__)

@flask_app.route('/alive')
def alive():
    return "I am alive!"

@flask_app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update and app:  # Ensure app exists before processing update
        logging.info(f"Received update: {update}")  # Debugging
        app.process_update(update)
    return "OK", 200  # Required response for Telegram

def run_flask():
    try:
        flask_app.run(host='0.0.0.0', port=10002)
    except OSError as e:
        if "Address already in use" in str(e):
            logging.error("Port 10002 in use! Trying alternate port 5000...")
            flask_app.run(host='0.0.0.0', port=5000)
        else:
            raise

async def main():
    await app.start()
    await asyncio.Event().wait()
    
# ========== clear.py logic merged here ==========
def clear_cache_and_sessions():
    folders_to_clear = ['.cache', '__pycache__', '.git']
    for folder in folders_to_clear:
        logging.info(f"Checking folder: {folder}")
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                logging.info(f"✅ Cleared folder: {folder}")
            except Exception as e:
                logging.error(f"❌ Error clearing {folder}: {e}")
        else:
            logging.warning(f"⚠️ Folder not found: {folder}")

def self_ping():
    while True:
        try:
            logging.info("🌐 Self-pinging...")
            requests.get("https://f-njat.onrender.com")  # Update if needed
            logging.info("✅ Ping successful")
        except Exception as e:
            logging.error(f"❌ Ping failed: {e}")
        time.sleep(60)

def start_clear_tasks():
    # Start scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(clear_cache_and_sessions, 'interval', minutes=60)
    scheduler.start()

    # Start self-ping
    Thread(target=self_ping, daemon=True).start()

# Start cache-clear + ping before starting bot
if __name__ == "__main__":
    # Clear + Ping Tasks
    start_clear_tasks()

    # Run Flask server in thread
    Thread(target=run_flask).start()

    # Run Bot
    asyncio.run(main())
