from random import randint
from EIVT_question import Question


class TrainingWorker:
    
    def __init__(self, vocab_worker):
        self.vocab_worker = vocab_worker
        self.max_question_variants = 3
        self.questions_count = 0

    
    def training_process(self):
        self.__training_prepare()
        if 0 == self.questions_count:
            return False
        else:
            random_verbs_list = self.vocab_worker.get_random_irregular_verbs(self.questions_count)
            questions_list = self.__create_questions(random_verbs_list)


    def __training_prepare(self):
        message = "Please, input how many questions you want to answer. Or 0 to exit:"
        try:
            self.questions_count = int(input(message))
            if self.questions_count > self.vocab_worker:
                self.questions_count = self.vocab_worker.get_iverbs_limit()
            elif self.questions_count < 1:
                self.questions_count = 0
        except ValueError:
            print(f"EIVT_ERROR: incorrect questions count, must be > 0! Or 0 to exit")


    def __create_questions(self, random_verbs_list):
        questions_list = []
        max_questions = len(random_verbs_list)
        for i in range(max_questions):
            current_question_variant = randint(0, self.max_question_variants)
            if 0 == current_question_variant:
                pass
            elif 1 == current_question_variant:
                pass
            elif 2 == current_question_variant:
                pass

        return questions_list
