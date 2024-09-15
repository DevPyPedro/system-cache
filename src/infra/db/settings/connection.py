import sqlite3
import os

from src.infra.db.interface.connection_interface import ISqlite

class SqliteDatabase(ISqlite):
    def __init__(self) -> None:
        self.__conn_path = os.path.join("src","infra","db","settings","database")
        self.__conn = None
        
    def __create_conn(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__conn_path)
    
    def get_conn(self)-> sqlite3.Connection:
        self.__conn = self.__create_conn()
        return self.__conn
    
    def __enter__(self):
        return self.get_conn()
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.__conn:
            self.__conn.close()
            self.__conn = None