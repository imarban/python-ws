# Python Workshop
The purpose of this workshop is to build an application written in Python to demonstrate the main characteristics of the language. After completing this workshop the attendee should know the set of tools which Python offers to ease the software development.

# Setting up your environment
- Install Python 2.7 (It is included in most Linux based OS and OSX).
  - Included version in OSX might be outdated, you should update it. Run `brew install python` to do that.
- Check if pip is installed with `pip --version`. Install it if it's necessary.
- Install Virtual Environment. `pip install virtualenv` should do the trick.
- Install Virtual Environment Wrapper. Please follow [virtualenvwrapper installation guide](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

# Application to build
A helper application in the interviewing process. The app should ask to the user for the interview stage and the technology that the candidate is applying for. After that, the application should show questions in a sequential way waiting for the input from the user for an evaluation for the candidate's answer (from 1 to 5). When there are no more questions the app should calculate the evaluation for the interviewee and show a summary with the final evaluation and the score for each question.

A question can be skipped leaving in blank the score.

# Setting up your workspace
- Create a virtual environment. Run `mkvirtualenv workshop`.

Now you are working in a separated workspace for this application. To exit this environment execute `deactivate`.

# Task 1 - Packages and modules
- Create a package named domain.
- Create a module named entities within **domain** package.
- Create a class Question within **entities** module.
  - The init method should receive the string for the question.
  - Set the content of the question to an instance variable.
- Create a class Interview within **entities** module.
  - The init method should receive the stage and technology for the interview as parameters in the init method.
  - Set the content of the parameters to instance variables
  - Create an instance variable with the current date and time. Check datetime module from Python.
  - Make sure the string representation for an Interview instance be "\<stage\> interview for \<technology\> profile applied on \<date\>".

# Task 2 - File handling
- Create a module named QuestionLoader.
- Create a class named QuestionLoaderFromTxtFile within the module created.
  - Create a load method which receives two parameters, the stage and the technology.
      - Implement the functionality for load method. It should open a file according the interview, read all the content and assign it to an instance variable named question_list.

# Task 3 - Iterators and generators
- Create a generator function in the QuestionLoaderFromTxtFile class which returns one **Question** instance at time. Read the questions from the instance variable created in the previous task. The name for this function must be questions.

# Task 4 - Completing Interview class
- Add a parameter in the init method of Interview entity named loader
- In the Interview's init method create an instance of loader, call its questions method and assign it to an instance variable named questions.
- Define the next_question method and return the next question from self.questions, in case there are no more questions return None

# Task 5 - Creating the front end
- Define a main.py module.
- Define a main function within **main** module.
- Read from the standard input the value for stage. Possible values are [screen, profile, pair].
  - Optional: Set a default value.
  - Optional: Validate for a possible stage.
- Read from the standard input the value for technology. Possible values are [java, python, ruby].
  - Optional: Set a default value.
  - Optional: Validate for a possible technology.
- Create an Interview instance using our implementation QuestionLoaderFromTxtFile.
- Add a print statement to make clear the interview is starting. Also, print the interview str method
- Print each question available in the interview and wait for the score from the user

# Task 6 - Exception and Errors - Property
- Add a list for scores in Interview class
- Create a method for adding a score in the list of scores.
  - Raise a ValueError in case a non integer, greater than 5 or lesser than 1 be received. Raise the error with an specific failure message.
- Create a property in the Interview class named score which returns the average for scores.

# Task 7 - Finishing the front end
- Add the score received in the Interview instance.
  - If a not valid score has been introduced then catch the error, print the message and allot the program to continue. Do **not** consider repeat the question or waiting for the correct value.
- Print the final score using the property defined.
