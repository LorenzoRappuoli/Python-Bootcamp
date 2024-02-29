class QuizBrain():

    def __init__(self, question_list):
        self.qnumber = 0
        self.qlist = question_list
        self.score = 0

    def still_has_question(self):
        if self.qnumber+1 < len(self.qlist):
            return True
        else:
            return False

    def next_question(self):
        q = self.qlist[self.qnumber].question
        risp = input(f"Q.{self.qnumber+1} : {q} (True/False)? ")
        answer = self.qlist[self.qnumber].answer
        #if risp == self.qlist[self.qnumber].answer:
        #    print("Right")
        #    self.score += 1
        #else:
        #    print("Mistake")

        self.check_answer(risp, answer)
        self.qnumber += 1

    def check_answer(self, u_ans, t_ans ):
        if u_ans.lower() == t_ans.lower():
            print("Right")
            self.score += 1
        else:
            print("False")



