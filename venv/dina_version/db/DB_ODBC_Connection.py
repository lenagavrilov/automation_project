import pyodbc

class DB_ODBC_Connection:

    def __init__(self):
        self.connection = pyodbc.connect(
            'Driver={ODBC Driver 13 for SQL Server};'
            'Server=DESKTOP-7FQ889E\SQLEXPRESS;'
            'Database=Automation;'
            'Trusted_Connection=yes;'
            # 'uid=sa;pwd=""'
        )
    def get_connection(self):
        return self.connection