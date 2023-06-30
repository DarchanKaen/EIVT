from random import randint
from src.EIVT_question import Question


class TrainingWorker:
    
    def __init__(self, vocab_worker):
        self.vocab_worker = vocab_worker
        self.max_question_variants = 3
        self.questions_count = 0
        self.iverb_delimiter = "/"

    
    def training_process(self):
        self.__training_prepare()
        if 0 == self.questions_count:
            return False
        else:
            random_verbs_list = self.vocab_worker.get_random_irregular_verbs(self.questions_count)
            questions_list = self.__create_questions(random_verbs_list)

            training_result = 0
            for i in range(self.questions_count):
                question = questions_list[i]
                print(f"~Question # {i + 1} / {self.questions_count}:")
                question_result = question.question_process()
                if True == question_result:
                    training_result += 1
            print(f"~~Correct answers: {training_result} / {self.questions_count}. \n\tTraining finished!")



    def __training_prepare(self):
        message = "Please, input how many questions you want to answer. Or 0 to exit: "
        try:
            self.questions_count = int(input(message))
            iverbs_limit = self.vocab_worker.get_iverbs_limit()
            if self.questions_count > iverbs_limit:
                self.questions_count = iverbs_limit
            elif self.questions_count < 1:
                self.questions_count = 0
        except ValueError:
            print(f"EIVT_ERROR: incorrect questions count, must be > 0! Or 0 to exit")


    def __create_questions(self, random_verbs_list):
        questions_list = []
        max_questions = len(random_verbs_list)
        for i in range(0, max_questions):
            current_iverb = random_verbs_list[i]
            current_question_variant = randint(0, self.max_question_variants)
            current_question_text = ""
            current_question_answer = []
            if 0 == current_question_variant:
                current_question_text = f"Please, type Form III of verb `{current_iverb[0]}`..."
                current_question_answer = self.__parse_question_answer(current_iverb[2])
            elif 1 == current_question_variant:
                current_question_text = f"Please, type Form II of verb `{current_iverb[0]}`..."
                current_question_answer = self.__parse_question_answer(current_iverb[1])
            elif 2 == current_question_variant:
                current_question_text = f"Please, type Form I of verb `{current_iverb[2]}`..."
                current_question_answer = self.__parse_question_answer(current_iverb[0])
            elif 3 == current_question_variant:
                current_question_text = f"Please, type Form I of verb `{current_iverb[1]}`..."
                current_question_answer = self.__parse_question_answer(current_iverb[0])
            current_question = Question(current_question_text, current_question_answer)
            questions_list.append(current_question)
        return questions_list


    def __parse_question_answer(self, iverb):
        parsed_answer = iverb.split(self.iverb_delimiter)
        return parsed_answer
