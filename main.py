from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

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
quiz = QuizBrain(question_bank) # QuizBrain have attribute of question_number default = 0, and
# question_list with all questions object in list
quiz.next_question() # quiz variable contain object QuizBrain with method next_question
# which do what?
# which print question_number equal 0 and question
