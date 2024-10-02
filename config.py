# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24935975"))
API_HASH = getenv("API_HASH", "0f628b53aba7debe2de4b24dd85c1a49")
BOT_TOKEN = getenv("BOT_TOKEN", "7492608277:AAFmkiUjO6e7tUZOgPw0rSqxfmWZ8g0rTmY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7593890865").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://karauraofficial:WDTStpioolgAgu7o@cluster0.vkalo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1430504486")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002174209085"))
