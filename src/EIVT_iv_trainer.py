from random import choice


class IVTrainer:
    def __init__(self, db_worker):
        self.db_worker = db_worker
        self.get_all_query = "SELECT * FROM eivt"
        self.all_iverbs_list = []
        self.random_iverbs_list = []


    def get_all_irregular_verbs(self):
        self.db_worker.connect()
        self.all_iverbs_list = self.db_worker.execute_and_return(self.get_all_query)
        self.db_worker.disconnect()


    def get_random_irregular_verbs(self, max_iverbs):
        self.__clear_previous_random_iverbs()
        random_indexes = self.__get_random_indexes(max_iverbs)
        for random_index in random_indexes:
            random_iverb = self.all_iverbs_list[random_index]
            random_iverb = (random_iverb[1], random_iverb[2], random_iverb[3])
            self.random_iverbs_list.append(random_iverb)


    def __clear_previous_random_iverbs(self):
        self.random_iverbs_list = []


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
     