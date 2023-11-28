'''module for connecting to an sql server and querying it'''
from pyodbc import Row, connect

class Sql:
    def __init__(self, con_string: str):
        self.connection = connect(con_string, autocommit = True, timeout = 10)


    def probe_rows(self, statement: str) -> list[Row]:
        return self.connection.cursor().execute(statement).fetchall()

    def probe_row(self, statement: str) -> Row | None:
        return self.connection.cursor().execute(statement).fetchone()

    def alter(self, statement: str):
        cursor = self.connection.cursor()
        cursor.execute(statement)

    def __del__(self):
        self.connection.close()

