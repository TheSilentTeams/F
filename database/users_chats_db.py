# users_chats_db.py

import motor.motor_asyncio
from info import (
    DATABASE_NAME, DATABASE_URI, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF,
    SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT, AUTO_DELETE, MAX_BTN, AUTO_FFILTER,
    SHORTLINK_API, SHORTLINK_URL, IS_SHORTLINK, TUTORIAL, IS_TUTORIAL
)

class Database:
    def __init__(self, client, database_name):
        self._client = client
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups

    def new_user(self, id, name):
        return {
            "id": id,
            "name": name,
            "ban_status": {"is_banned": False, "ban_reason": ""}
        }

    def new_group(self, id, title):
        return {
            "id": id,
            "title": title,
            "chat_status": {"is_disabled": False, "reason": ""}
        }

    async def add_user(self, id, name):
        await self.col.insert_one(self.new_user(id, name))

    async def is_user_exist(self, id):
        return bool(await self.col.find_one({'id': int(id)}))

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def remove_ban(self, id):
        await self.col.update_one({'id': id}, {'$set': {'ban_status': {"is_banned": False, "ban_reason": ""}}})

    async def ban_user(self, user_id, ban_reason="No Reason"):
        await self.col.update_one({'id': user_id}, {'$set': {'ban_status': {"is_banned": True, "ban_reason": ban_reason}}})

    async def get_ban_status(self, id):
        default = {"is_banned": False, "ban_reason": ""}
        user = await self.col.find_one({'id': int(id)})
        return user.get('ban_status', default) if user else default

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def get_banned(self):
        users = self.col.find({'ban_status.is_banned': True})
        chats = self.grp.find({'chat_status.is_disabled': True})
        b_users = [user['id'] async for user in users]
        b_chats = [chat['id'] async for chat in chats]
        return b_users, b_chats

    async def add_chat(self, chat, title):
        await self.grp.insert_one(self.new_group(chat, title))

    async def get_chat(self, chat):
        doc = await self.grp.find_one({'id': int(chat)})
        return doc.get('chat_status') if doc else False

    async def re_enable_chat(self, id):
        await self.grp.update_one({'id': int(id)}, {'$set': {'chat_status': {"is_disabled": False, "reason": ""}}})

    async def update_settings(self, id, settings):
        await self.grp.update_one({'id': int(id)}, {'$set': {'settings': settings}})

    async def get_settings(self, id):
        default = {
            'button': SINGLE_BUTTON,
            'botpm': P_TTI_SHOW_OFF,
            'file_secure': PROTECT_CONTENT,
            'imdb': IMDB,
            'spell_check': SPELL_CHECK_REPLY,
            'welcome': MELCOW_NEW_USERS,
            'auto_delete': AUTO_DELETE,
            'auto_ffilter': AUTO_FFILTER,
            'max_btn': MAX_BTN,
            'template': IMDB_TEMPLATE,
            'shortlink': SHORTLINK_URL,
            'shortlink_api': SHORTLINK_API,
            'is_shortlink': IS_SHORTLINK,
            'tutorial': TUTORIAL,
            'is_tutorial': IS_TUTORIAL
        }
        chat = await self.grp.find_one({'id': int(id)})
        return chat.get('settings', default) if chat else default

    async def disable_chat(self, chat, reason="No Reason"):
        await self.grp.update_one({'id': int(chat)}, {'$set': {'chat_status': {"is_disabled": True, "reason": reason}}})

    async def total_chat_count(self):
        return await self.grp.count_documents({})

    async def get_all_chats(self):
        return self.grp.find({})

    async def get_db_size(self):
        return (await self.db.command("dbstats"))['dataSize']


# 🔧 Lazy-loaded globals to avoid event loop issues
client = None
db = None

async def init_db():
    global client, db
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
    db = Database(client, DATABASE_NAME)
