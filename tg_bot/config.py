import os
from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = os.getenv('OWNER_ID')  # my telegram ID
    OWNER_USERNAME = os.getenv('OWNER_USERNAME')  # my telegram username
    API_KEY = os.getenv('API_KEY')  # my api key, as provided by the botfather
    USE_MESSAGE_DUMP = os.getenv('USE_MESSAGE_DUMP')
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
