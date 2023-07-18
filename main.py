from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQuestion = Question(question_text, question_answer)
    question_bank.append(newQuestion)

# print(question_bank[3].text)
# print(question_bank[3].answer)
