from __future__ import division
import datetime

class Question(object):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class Interview(object):
    def __init__(self, stage, technology, loader):
        self.date = datetime.datetime.now()
        self.stage = stage
        self.technology = technology
        self.scores = []
        self.questions = loader(stage, technology).questions()

    def next_question(self):
        return next(self.questions, None)

    def add_score(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Not an integer")

        if not(1 <= value <= 5):
            raise ValueError("Score not valid")
        else:
            self.scores.append(value)

    @property
    def score(self):
        return sum(self.scores, 0) / len(self.scores)

    def __str__(self):
        return "{0} interview for {1} profile applied on {2} ".format(self.stage, self.technology, self.date.strftime('%m/%d/%Y'))
