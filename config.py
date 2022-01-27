import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "aruack")
ALIVE_NAME = getenv("ALIVE_NAME", "Aruack")
BOT_USERNAME = getenv("BOT_USERNAME", "yulia_vcbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "yulia_vcmusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Aruacksupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "aruackofficial")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/aruack/videostream")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/290fe5742441b94a132da.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "  ")
IMG_2 = getenv("IMG_2", "  ")
IMG_3 = getenv("IMG_3", "  ")
