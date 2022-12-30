#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5632300210:AAH7BJQYJocKeyk_7BIYJsI2j7b0EIw26V0")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19751208"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "
7ee46e0888432fad23173820d4caddf2")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOLsBu8My1rx6M8tpfWOVdH3R2DbDh12E11T3q64oY8p9T3J0erY9i0tL-YFzOtPOVnwVebeYxy--wN8B2OIVMwISmhtgtTZ03NwNFPjwdExVp1n9EgqXaUGmTs9wH3CoqW_-_oB405svEfCXv-E4wNYRxsox1CM9i74a9J4RFSaFmdnG9e6CfV8PC-B-syAgbQMT9MftwBe4k5l1F4I3niwYA6El8Vw9rxuZYVrJDkHWgB8VLcQYYhoC1eNZE2ruA-Nf9XlplO47HFINFoBy2xNVkJsgU3MpVNwJJJnRq5hvK5Z-qYwm-Go0ve3wzMFEPG6o2HLSI1u_w0qv2wDPvtZK3YQ=")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://clonetgbot:clonetgbot@cluster0.v8hwx1m.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
