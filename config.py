import os
from os import getenv

from dotenv import load_dotenv
from redis_dict import RedisDict

redis = RedisDict('users')
# database.clear()
# print(user_id)
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
