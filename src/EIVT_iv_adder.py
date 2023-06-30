class IVAdder:
    def __init__(self, db_worker):
        self.db_worker = db_worker
        self.info_message = "Enter irregular verb in format 'form_I form_II form_III'. \n\tOr type 'e' (or 'exit') to exit. \n\tOr type 'i' (or 'info') to info."
        self.max_iv_length = 3
        self.add_query = "INSERT INTO eivt (form_I, form_II, form_III) VALUES (?, ? ,?)"
        pass

    def add_process(self):
        print(self.info_message)
        self.db_worker.connect()
        while True:
            user_input = input("Enter irregular verb(or 'i' to info): ").lower()
            if 'e' == user_input or 'exit' == user_input:
                self._exit_add_process()
                break
            elif 'i' == user_input or 'info' == user_input:
                print(self.info_message)
            else:
                self._add_irregular_verb(user_input)

    def _exit_add_process(self):
        self.db_worker.disconnect()

    def _add_irregular_verb(self, iv_string):     
        iv_splitted = iv_string.split()
        if len(iv_splitted) != self.max_iv_length:  
            print(f"EIVT_ERROR: incorrect words count, must be {self.max_iv_length}")
            return False
        self.db_worker.execute(self.add_query, (iv_splitted[0], iv_splitted[1], iv_splitted[2]))

