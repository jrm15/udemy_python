student_scores = {
    'Harry' : 81,
    'Ron' : 78,
    'Hermione' : 99,
    'Draco' : 74,
    'Neville' : 62
}

def grades_of_scores(score : int) -> str:
    result = ''
    if score <= 70 :
        result = 'Fail'
    elif score <= 80:
        result = 'Acceptable'
    elif score <= 90:
        result = 'Exceeds Expectations'
    else:
        result = 'Outstanding'
    return result

for key in student_scores:
        print(key + ': ', end = '')
        print(grades_of_scores(student_scores[key]))