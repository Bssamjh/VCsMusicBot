import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "6256153474:AAHn8sf8VtJwQkHcAvaOTXpeZ3B9mmKQgAM")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tsaewm")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "26327266"))
API_HASH = getenv("API_HASH", "2c204ae0d9e0853bdf39fce51aa96129")
BOT_USERNAME = getenv("BOT_USERNAME", "musiccxzesawe_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "cxzftds")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", “6021847554“).split()))
