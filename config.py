import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("7652311090:AAFocVbw22rHXpiikv24IKgCJy4LveRSY1I")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("22865155"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("e430e3f61712616b926be959f1612c46")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("1002851667345"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("mongodb+srv://adarshppandey937:uIoPcln9vXQBF0vP@cluster0.o9mn6hb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "beastxsrcb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
