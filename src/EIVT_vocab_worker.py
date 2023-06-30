from random import choice


class VocabWorker:
    
    def __init__(self, db_worker):
        self.db_worker = db_worker
        self.max_iv_length = 3
        self.select_all_query = "SELECT form_I, form_II, form_III FROM eivt"
        self.add_query = "INSERT INTO eivt (form_I, form_II, form_III) VALUES (?, ? ,?)"
        self.all_iverbs_list = []
        self.random_iverbs_list = []


    def add_process(self):
        self.db_worker.connect() 
        while True:
            user_input = input("Enter irregular verb(or 'i' to info / 'e' to exit): ").lower()
            if 'e' == user_input or 'exit' == user_input:
                self.exit_add_process()
                break
            elif 'i' == user_input or 'info' == user_input:
                print(self.info_message)
            else:
                self.add_irregular_verb(user_input)


    def add_irregular_verb(self, iv_string):   
        self.get_all_irregular_verbs() 
        self.db_worker.connect() 
        iv_splitted = iv_string.split()
        if len(iv_splitted) != self.max_iv_length:  
            print(f"EIVT_ERROR: incorrect words count, must be {self.max_iv_length}")
            self.exit_add_process()
            return False
        else:
            iverb_tuple = (iv_splitted[0], iv_splitted[1], iv_splitted[2])
            if iverb_tuple not in self.all_iverbs_list:
                self.db_worker.execute(self.add_query, iverb_tuple) 
            else:
                print(f"EIVT_ERROR: this verb already exist!")
            self.exit_add_process()


    def get_all_irregular_verbs(self):
        self.db_worker.connect()
        self.all_iverbs_list = self.db_worker.execute_and_return(self.select_all_query)
        self.db_worker.disconnect()


    def get_random_irregular_verbs(self, max_iverbs):
        self.get_all_irregular_verbs() 
        self.random_iverbs_list = []
        random_indexes = self.__get_random_indexes(max_iverbs)
        for random_index in random_indexes:
            random_iverb = self.all_iverbs_list[random_index]
            #random_iverb = (random_iverb[1], random_iverb[2], random_iverb[3])
            self.random_iverbs_list.append(random_iverb)
        print("random_iverbs:", self.random_iverbs_list)


    def exit_add_process(self):
        self.db_worker.disconnect()


    def __get_random_indexes(self, max_iverbs):
        limit = len(self.all_iverbs_list)
        if max_iverbs > limit or max_iverbs < 1:
            max_iverbs = limit
        all_indexes_list = list(range(limit))
        random_idexes_list = []
        for _ in range(max_iverbs):
            random_index = choice(all_indexes_list)
            random_idexes_list.append(random_index)
            all_indexes_list.remove(random_index)
        return random_idexes_list