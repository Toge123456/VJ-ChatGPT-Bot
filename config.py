import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29539483"))
API_HASH = environ.get("API_HASH", "ab57ccd3de7bbb16058a80b179ac4294")
BOT_TOKEN = environ.get("BOT_TOKEN", "6935511939:AAGysFC0HP-lOwBTQvkw2pTS-u0MGENP0Ys")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "29539483"))
DB_URI = environ.get("DB_URI", "mongodb+srv://toge3260:QO4ozHWxuoQeHsry@cluster0.4bedvpu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), True)
