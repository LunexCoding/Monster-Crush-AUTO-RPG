HP = 2
damage = 15

import pymysql
from config import host, port, user, password, database


db_config = {
    'host': host,
    'port': port,
    'user': user,
    'password': password,
    'database': database,
    'cursorclass': pymysql.cursors.DictCursor
}


class DatabaseConnection(object):
    def __init__(self, db_local):
        self.db_local = db_local
        self.db_conn = None
        self.db_cursor = None

    def __enter__(self):
        self.db_conn = pymysql.connect(**self.db_local, autocommit=True)
        self.db_cursor = self.db_conn.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closable.')
           return True # exception handled successfully

    def get_row(self, sql, data = None):
        self.db_cursor.execute(sql)
        self.resultset = self.db_cursor.fetchall()
        return self.resultset


sql = "SELECT * FROM users LIMIT 10"

# with DatabaseConnection(db_config) as test:
#     resultSet = test.get_row(sql)
#     print(resultSet)

databaseCon = DatabaseConnection(db_config)

with databaseCon as test:
    resultSet = test.get_row(sql)
    print(resultSet)