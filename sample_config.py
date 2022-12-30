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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOIUBuxFyf670u4hfE_n69_oRqZMd2HQm-BT_CHYEJLh9r4d4AG6U-yN1c3dPCkySsZ55Tlicyo74ukoYMRp8EjxesjfJO0I0OsliS5P26B5w5zr13MphGdvYzUvhGLEMueue1oewYQlFsAJ5kbiqUa2O1QBw5-h11N8Uwq9AmBnmiMAvV-YPkQ9fpq429B3rA22iQftKU8FnU3kICzt6gDrXXW8EqlklViD3ejQZflDMslyEf_5BgZ7sUpa3fB8yG7T4l50PD6hskpH_yhwmiQj5XaS-v-5qnqrr3nxoRCl2I9Qv5QkgkcUVV2b6VxEidT8m2OfX1eCX-l3vJVMyiML15CQ=")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://clonetgbot:clonetgbot@cluster0.v8hwx1m.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
