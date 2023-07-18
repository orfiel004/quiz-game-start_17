from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    # from dictionary with key "text" assign value in to question_text
    question_answer = question["answer"]
    newQuestion = Question(question_text, question_answer)
    # create new object Question witch attribute from question_text variable
    question_bank.append(newQuestion)

# print(question_bank[3].text)
# print(question_bank[3].answer)
