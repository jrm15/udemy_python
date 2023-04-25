class Comprobe:
    def __init__(self, answer):
        self.answer = answer

    def result(self, result) -> bool:
        if result == self.answer:
            return True
        else:
            return False
