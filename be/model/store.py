import logging
from pymongo import MongoClient

class Store:
    client: MongoClient
    db: str

    def __init__(self, db_uri):
        self.client = MongoClient(db_uri)
        self.db = self.client.get_database("bookstore")

    def init_tables(self):
        try:
            # 创建用户表
            self.db.create_collection("user")
            self.db.user.create_index("user_id", unique=True)

            # 创建用户商店关联表
            self.db.create_collection("user_store")
            self.db.user_store.create_index([("user_id", 1), ("store_id", 1)], unique=True)

            # 创建商店表
            self.db.create_collection("store")
            self.db.store.create_index([("store_id", 1), ("book_id", 1)], unique=True)

            # 创建新订单表
            self.db.create_collection("new_order")
            self.db.new_order.create_index("order_id", unique=True)

            # 创建新订单详情表
            self.db.create_collection("new_order_detail")
            self.db.new_order_detail.create_index([("order_id", 1), ("book_id", 1)], unique=True)

        except Exception as e:
            logging.error(e)

    def get_db_conn(self):
        return self

database_instance: Store = None

def init_database(db_uri):
    global database_instance
    database_instance = Store(db_uri)

def get_db_conn():
    global database_instance
    return database_instance.get_db_conn()



# import logging
# import os
# import sqlite3 as sqlite
#
# class Store:
#     database: str
#
#     def __init__(self, db_path):
#         self.database = os.path.join(db_path, "be.db")
#         self.init_tables()
#
#     def init_tables(self):
#         try:
#             conn = self.get_db_conn()
#             conn.execute(
#                 "CREATE TABLE IF NOT EXISTS user ("
#                 "user_id TEXT PRIMARY KEY, password TEXT NOT NULL, "
#                 "balance INTEGER NOT NULL, token TEXT, terminal TEXT);"
#             )
#
#             conn.execute(
#                 "CREATE TABLE IF NOT EXISTS user_store("
#                 "user_id TEXT, store_id, PRIMARY KEY(user_id, store_id));"
#             )
#
#             conn.execute(
#                 "CREATE TABLE IF NOT EXISTS store( "
#                 "store_id TEXT, book_id TEXT, book_info TEXT, stock_level INTEGER,"
#                 " PRIMARY KEY(store_id, book_id))"
#             )
#
#             conn.execute(
#                 "CREATE TABLE IF NOT EXISTS new_order( "
#                 "order_id TEXT PRIMARY KEY, user_id TEXT, store_id TEXT)"
#             )
#
#             conn.execute(
#                 "CREATE TABLE IF NOT EXISTS new_order_detail( "
#                 "order_id TEXT, book_id TEXT, count INTEGER, price INTEGER,  "
#                 "PRIMARY KEY(order_id, book_id))"
#             )
#
#             conn.commit()
#         except sqlite.Error as e:
#             logging.error(e)
#             conn.rollback()
#
#     def get_db_conn(self) -> sqlite.Connection:
#         return sqlite.connect(self.database)
#
#
# database_instance: Store = None
#
#
# def init_database(db_path):
#     global database_instance
#     database_instance = Store(db_path)
#
#
# def get_db_conn():
#     global database_instance
#     return database_instance.get_db_conn()
