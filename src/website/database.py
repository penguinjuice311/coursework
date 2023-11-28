from typing import Protocol
from pyodbc import Row 


class Sql(Protocol):

    def probe_rows(self, statement: str) -> list[Row]:
        ... 

    def probe_row(self, statement: str) -> Row | None:
        ...

    def alter(self, statement: str):
        ...

    def __del__(self):
        ...


class Database:
    def __init__(self, sql: Sql):
        self.sql = sql
