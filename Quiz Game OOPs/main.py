from question_model import Question
from data import question_data
from quiz_brain import QuizBrains
from art import logo


print(logo)
question_bank = []

for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrains(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have finished the program")
print(f"Your final score was {quiz.score}/{quiz.question_number} ")
