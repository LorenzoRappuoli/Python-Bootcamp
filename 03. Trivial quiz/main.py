from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


qlist = []
for q in question_data:
    question = Question(q['text'],q['answer'])
    qlist.append(question)

Brain = QuizBrain(qlist)

while Brain.still_has_question():
    Brain.next_question()
print(f"Final score {Brain.score}")