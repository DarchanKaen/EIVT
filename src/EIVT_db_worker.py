import sqlite3


class DBWorker:
    def __init__(self):
        self.db_name = "eivt_db"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def execute(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def createTable(self):
        try:
            create_table_query = "CREATE TABLE eivt (id INTEGER PRIMARY KEY AUTOINCREMENT, form_I TEXT, form_II TEXT, form_III TEXT)"
            self.cursor.execute(create_table_query)
        except BaseException:
            print("EIVT_WARNING: eivt table already exist.")



