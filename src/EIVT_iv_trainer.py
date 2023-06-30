class IVTrainer:
    def __init__(self, db_worker):
        self.db_worker = db_worker
        self.get_all_query = "SELECT * FROM eivt"


    def get_all_irregular_verbs(self):
        self.db_worker.connect()
        selection_result = self.db_worker.execute_and_return(self.get_all_query)
        print("selection_result:")
        print(selection_result)

    #if "__main__" == __name__:
    #    print("!")
