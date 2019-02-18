import sqlite3
from crawler.settings import SQLITE_DB_URI
# print(SQLITE_DB_URI)

class Db :
    __instance = None

    sqlite_uri = SQLITE_DB_URI

    def execute(self,sql):
        try:

            return self.__cur.execute(sql)

        except Exception as e:

            print('Sqlite 错误:',e)

    def commit(self):

        self.__con.commit()


    def close(self):

        self.__con.close()


    def __new__(cls, *args, **kwargs):

        if cls.__instance == None:

            cls.__con = sqlite3.connect(cls.sqlite_uri)

            cls.__cur = cls.__con.cursor()

            cls.__instance = object.__new__(cls)

        return cls.__instance

sqlite = Db()
