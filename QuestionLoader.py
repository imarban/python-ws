from domain.entities import Question

class QuestionLoaderFromTxtFile(object):
    def __init__(self, stage, technology):
        self.load(stage, technology)

    def load(self, stage, technology):
        with open('questions/{0}/{1}.txt'.format(technology, stage)) as content:
            self.question_list = content.read().splitlines()


    def questions(self):
        for question in self.question_list:
            yield Question(question)
