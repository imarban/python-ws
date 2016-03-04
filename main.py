from domain.entities import Interview
from QuestionLoader import QuestionLoaderFromTxtFile

def main():
    stage = raw_input("What stage are you going to interview? Possible values are screen profile pair (screen): ") or "screen"

    profile = raw_input("What profile are you going to interview? Possible values: " +
    "\njava\npython\nruby (java): ") or "java"

    interview = Interview(stage, profile, QuestionLoaderFromTxtFile)

    print interview

    print "------- {0} - {1} -------".format(profile.upper(), stage.upper())
    print "For each question please input your score from 1 to 5"

    question = interview.next_question()

    while question:
        score = raw_input(str(question) + ": ")
        try:
            interview.add_score(score)
        except ValueError as ve:
            print ve.message
        question = interview.next_question()

    print "There are no more questions"
    print "The score for the interviewee is: {!s} ".format(interview.score)


main()
