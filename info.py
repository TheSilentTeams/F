#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧ 

import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', 16536417))
API_HASH = environ.get('API_HASH', "f6e58a549da642d7b765744a2f82c6d9")
BOT_TOKEN = environ.get('BOT_TOKEN', "")


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/e8876d6689b687de24fbe.png')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/e8876d6689b687de24fbe.png")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/6657f10a33d40c047f875.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/7db384d955159386d1060.jpg")
VRFY_IMG = environ.get("VRFY_IMG", "https://graph.org/file/cf2a38e916d9388212ec7.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '921365334').split()]
CHANNELS = environ.get('CHANNELS', '-1001976969484')
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '921365334 1153569236').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001953320653')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://robo123:robo123@cluster0.pana52z.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "New_auto_bot_may_2025")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'NewStart')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'adrinolinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '5e84201806979b3ab22725bd996d187a20ca7f8c')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+V-VVLTPERHM4YWY9')
SPRT_GRP = environ.get('SPRT_GRP', 'https://t.me/+ZSUTmOXuwqxlODk1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/THE_SILENT_TEAMS')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Robo_5_0/73')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/Robo_5_0/73')
MSG_ALRT = environ.get('MSG_ALRT', 'ᴄʜᴀʜᴛᴇ ᴋʏᴀ ʜᴏ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001539400248'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'THE_SILENT_TEAMS')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "[{file_name}](https://t.me/The_Silent_Teams)\n\n<b>Join Our Offical Channel & Group @The_Silent_Teams ❤️") # f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

# Online Stream and Download
# NO_PORT = bool(environ.get('NO_PORT', False))
# APP_NAME = None
# if 'DYNO' in environ:
#     ON_HEROKU = True
#     APP_NAME = environ.get('APP_NAME')
# else:
#     ON_HEROKU = False
# BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
# FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
# URL = "https://unknown--ibot-991747530105.herokuapp.com/".format(FQDN) if ON_HEROKU or NO_PORT else \
#     "https://unknown--ibot-991747530105.herokuapp.com/".format(FQDN, PORT)
# SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
# WORKERS = int(environ.get('WORKERS', '4'))
# SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
# MULTI_CLIENT = False
# name = str(environ.get('name', 'LazyPrincess'))
# PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
# if 'DYNO' in environ:
#     ON_HEROKU = True
#     APP_NAME = str(getenv('APP_NAME'))

# else:
#     ON_HEROKU = False
# HAS_SSL=bool(getenv('HAS_SSL',False))
# if HAS_SSL:
#     URL = "https://unknown--ibot-991747530105.herokuapp.com/".format(FQDN)
# else:
#     URL = "https://unknown--ibot-991747530105.herokuapp.com/".format(FQDN)



LANGUAGES = ["marathi", "mar", "gujarati", "guj", "malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

QUALITY = ["240P", "360P", "480P", "560P", "720P" ,"1080P", "2160P"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]




LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
