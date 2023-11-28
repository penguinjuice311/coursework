from pyodbc import Row, connect

class Sql:
    def __init__(self, con_string: str):
        pass

    def probe_rows(self, statement: str) -> list[Row]:
        pass

    def probe_row(self, statement: str) -> Row | None:
        pass

    def alter(self, statement: str):
        pass

    def __del__(self):
        pass
