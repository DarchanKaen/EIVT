class Question:

    def __init__(self, question_text, question_answers):
        self.text = question_text
        self.answers = question_answers
        self.is_asked = False
        self.is_answered = False
        self.is_correct_answered = False;


    def is_user_answer_correct(self, user_answer):
        is_correct = False
        if user_answer.strip().lower() in self.answers:
            is_correct = True
            self.is_correct_answered = True
        self.is_answered = True
        return is_correct

        