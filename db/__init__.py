from pymongo import MongoClient
from config.default import config

client = MongoClient(config.db_host, config.db_name)
db = client['testDb']