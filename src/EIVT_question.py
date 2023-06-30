class Question:

    def __init__(self, question_text, question_answers):
        self.text = question_text
        self.answers = question_answers
        self.is_asked = False
        self.is_answered = False
        self.is_correct_answered = False;


    def question_process(self):
        message = f"{self.text}"
        while True:
            user_answer = input(message)
            is_correct = self.__is_user_answer_correct(user_answer)
            if True == is_correct:
                message = "\t...this is correct!"
            else:
                answer_as_text = "".join(self.answers)
                message = f"\t...this is wrong. Correct answer is: {answer_as_text}"
            print(message)
            break
        return is_correct


    def __is_user_answer_correct(self, user_answer):
        is_correct = False
        if user_answer.strip().lower() in self.answers:
            is_correct = True
            self.is_correct_answered = True
        self.is_asked = True
        self.is_answered = True
        return is_correct

        