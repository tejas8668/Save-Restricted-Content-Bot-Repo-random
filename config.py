# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6018060368"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://tejaschavan1110:jkZSAYN4iWHRq1CM@cluster0.trwix.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002465239145"))
FORCESUB = getenv("FORCESUB", "-1002465239145")
