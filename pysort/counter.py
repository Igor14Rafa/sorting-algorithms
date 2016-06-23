

class Counter():
    def __init__(self):
        self.value = 0

    def next(self):
        value = self.value
        self.value += 1

        return value

    def zero(self):
        self.value = 0

counter = Counter()
