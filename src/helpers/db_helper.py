from pymongo import MongoClient
from bson.objectid import ObjectId

from src.config.config import Config
from src.helpers.date_helper import DateHelper

class DBHelper:
    def __init__(self):
        self._config = Config()
        self._db_server = self._config.get_db_server()
        self._db_port = self._config.get_db_port()
        self._db_database = self._config.get_db_database()
        self._client = MongoClient(self._db_server, self._db_port)
        self._date_helper = DateHelper()

    def _open(self, colletion_name):
        db = self._client[self._db_database]
        collection = db[colletion_name]
        return collection

    def _close(self):
        self._client.close()

    def insert(self, colletion_name, item):
        collection = self._open(colletion_name)

        item["is_enabled"] = True
        item["created_at"] = self._date_helper.now()

        result = collection.insert(item)
        self._close()
        return result

    def get(self, colletion_name, filters, sort=[["_id", 1]]):
        collection = self._open(colletion_name)

        filters["is_enabled"] = True

        result = collection.find(filters).sort(sort)
        items = list(result)
        self._close()
        return items

    def update(self, colletion_name, filters, entity):
        collection = self._open(colletion_name)
        entity["$set"]["updated_date"] = self._date_helper.now()
        result = collection.update_many(filters, entity)
        self._close()
        return result

    def delete(self, colletion_name, filters):
        collection = self._open(colletion_name)
        result = collection.delete_many(filters)
        self._close()
        return result

    @staticmethod
    def to_object_id(id):
        return ObjectId(id)
