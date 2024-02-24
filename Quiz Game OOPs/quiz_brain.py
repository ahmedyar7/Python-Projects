class QuizBrains:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    ## Methods:
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q{self.question_number} {current_question.text} True/False "
        ).lower()
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right, {self.score}")
        else:
            print("Wrong")
            print(f"Correct answer = {correct_answer}")
