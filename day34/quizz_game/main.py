from comprobe_result import Comprobe
from data import Question

api = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "category": 21,
    "type": "boolean"}

trivial = Question()


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
    print(trivial.question(api, parameters))
    answer = trivial.result(api, parameters)
    result = str(input('True or False?: '))
    comprobe = Comprobe(answer)
    result = comprobe.result(result)
    score_total = score(result, score_total)
    finaly = final(score_total)