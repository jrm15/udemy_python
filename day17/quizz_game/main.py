from comprobe_result import Comprobe
from data import question_data
import random


def question():
    number_aleat = int(random.randrange(1, 13))
    text = question_data[number_aleat]["text"]
    answer = question_data[number_aleat]["answer"]
    print (text)
    return answer


def score(answ, score):
    score[1] += 1
    if answ:
        score[0] += 1
        print(f'You got it right!\nThe correct answer was {answer}.\nYour current score is: {score}')
    else:
        print(f"That's wrong.\nThe correct answer was: {answer}.\nYour current score is: {score}")
    return score


def final(score):
    if score[0] != score[1]:
        return False
    else:
        return True


score_total = [0, 0]
finaly = True
while finaly:
    answer = question()
    result = str(input('True or False?: '))
    comprobe = Comprobe(answer)
    result = comprobe.result(result)
    score_total = score(result, score_total)
    finaly = final(score_total)