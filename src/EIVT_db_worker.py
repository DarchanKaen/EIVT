import sqlite3



class DBWorker:

    def __init__(self):
        self.db_name = "eivt_db"
        self.connection = None
        self.cursor = None
        self.createTable()


    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()


    def disconnect(self):
        self.connection.close()


    def execute(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()


    def execute_and_return(self, query, params = None):
        if None != params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        execution_result = self.cursor.fetchall()
        return execution_result


    def createTable(self):
        try:
            self.connect()
            create_table_query = "CREATE TABLE eivt (id INTEGER PRIMARY KEY AUTOINCREMENT, form_I TEXT, form_II TEXT, form_III TEXT)"
            self.cursor.execute(create_table_query)
            self.disconnect()
            print("EIVT_INFO: EIVT table created successfully!")
        except BaseException:
            print("EIVT_INFO: eivt table already exist.")



