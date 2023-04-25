import requests
import random


class Question:

    def question(self, api, parameters):
        num_aleat = int(random.randrange(0, 10))
        response = requests.get(api, params=parameters)
        data = response.json()
        question = (data['results'][num_aleat]['question'])
        return question

    def result(self, api, parameters):
        response = requests.get(api, params=parameters)
        data = response.json()
        result = (data['results'][0]['correct_answer'])
        return result
