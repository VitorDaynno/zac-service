from pymongo import MongoClient


from src.config.config import Config


class DB:
    def __init__(self):
        self.__config = Config()
        self.__db_server = self.__config.get_db_server()
        self.__db_port = self.__config.get_db_port()
        self.__db_database = self.__config.get_db_database()
        self.__client = MongoClient(self.__db_server, self.__db_port)

    def _open(self, colletion_name):
        db = self.__client[self.__db_database]
        collection = db[colletion_name]
        return collection

    def _close(self):
        self.__client.close()

    def insert(self, colletion_name, item):
        collection = self._open(colletion_name)
        result = collection.insert(item)
        self._close()
        return result
