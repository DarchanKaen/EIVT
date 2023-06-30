class Question:

    def __init__(self, question_text, question_answers):
        self.text = question_text
        self.answers = question_answers
        self.is_asked = False


    def is_user_answer_correct(self, user_answer):
        is_correct = False
        if user_answer in self.answers:
            is_correct = True
        return is_correct