# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we`re the end of quiz
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list # all question wil be here in object QuizBrain

    def next_question(self):
        # current_question wil contain object from question_list with number 0
        current_question = self.question_list[self.question_number]
        print(current_question.text)
        print(self.question_number)
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
