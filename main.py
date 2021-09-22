# I import random library to be able to use shuffle method, in this way I will be able to to order the questions randomly
import random
# I import collections to be able to use OrderedDict (ordered dictionary that will help me to sort the results easier than using a loop)
import collections

# input the name of first player
player_name = str(input("Enter your name: "))
# I validate the correctness of the name
# Check if it has only English characters <isalpha method>, no numbers (I deleted the spaces for verification)
# Also check if the user entered something
# I put everything in a while loop because I want to check as long as the input is not correct
while (player_name.strip().replace(" ", "").isalpha() == False or player_name == ""):
    player_name = input("Enter a valid name: ")
# for questions and answers I choose to use dictionary because I considered it to be the best representation
# due to the relation key-element will represent exactly the relation question-answer
questions_and_answers = {
    "1+1": "2",
    "What will be the last value of i at the end of: for i in range(0,10)...": "9",
    "What will be the result of 123%10?": "3",
    "What will be the result of 123/10?": "12",
    "2+2": "4",
    "3+2": "5",
    "What are WWW stands for?": "Wordl Wide Web",
    "What are FTP stands for?": "File Transfer Protocol",
    "Do you want the point ex officio?": "yes",
    "What are LAN stands for": "Local Area Network"
}
# I was offered the option to choose a standard 10-question test or a personalized one
test_mode = input("Do you want the default test?(10 questions)y/n ")
# again I took into account any errors, so until I get an answer of "y" or "n" I keep asking for it in the while loop
while (test_mode != "y" and test_mode != "n"):
    test_mode = input("Please input a valid value! y/n ")
if (test_mode == "n"):
    # if the user choose to don't answer all 10 question, I ask him how many questions do he want to ask to
    test_mode = input("Please enter the number of questions you would like to have ")
    ok = 1
    # I took into account any errors: no input, no numeric input, negative numbers, and I use try and except
    # to not stop the program from working and to continue until the user will write a valid value
    while (ok == 1):
        try:
            test_mode = int(test_mode)
            if (test_mode <= 0):
                test_mode = input("Please enter a valid number of questions ")
                continue
            ok = 0
        except ValueError:
            test_mode = input("Please enter a valid number of questions ")
else:
    # if the user want a 10 questions test, then test_mode will contain number 10
    # I use len method to be more general, in case in the future I want to add 100 questions
    test_mode = len(questions_and_answers)
# I don't find a way to shuffle my dictionary, so I put it in a list, shuffle the list, and put everything back in dictionary
temporary_list = list(questions_and_answers.items())
random.shuffle(temporary_list)
questions_and_answers = dict(temporary_list[0:test_mode:1])
# I create an empty dictionary where I will save the results for every attempt of the quiz
quiz_results = dict()
# In the variable average_score I will sum up the score of all the users. This will help me later to find the average score
average_score = 0


# I created a function in which I go through the questions in the test and save the answers and the score
def quiz(name):
    # I need to initialize the quiz_results and average_score variables as global, not just for local use
    global quiz_results
    global average_score
    # I will need a counter to track each correct answer, so I create a new variable and initialize with 0 at the beginning
    correct = 0
    # I iterate through every single question using for loop
    for key in questions_and_answers:
        # I display the question for users on the screen
        print(key)
        print("Type your answer and press Enter: ")
        answer = input()
        # I make sure the user enters an answer
        while (answer == ""):
            answer = input("Please answer: ")
        # I check the user's answer with the actual answer, to be more accurate I lowercase every letter and also deleted eventually extra blank spaces
        if (questions_and_answers[key].strip().lower() == answer.strip().lower()):
            # If the answer were correct, I count it, and notify the user
            correct += 1
            print("Correct!")
        else:
            # If the answer were wrong, I let the user know that, and also display the right answer
            print("Wrong, the answer was: ", questions_and_answers[key])
    # After the quiz is over, I let the user know how many correct answer he did, also as a percentage, also as a grade/10
    if (correct != 0):
        print("Congrats ", name, " you answer correct to: ", correct, " questions per ", len(questions_and_answers))
        print("The percentage score", correct * 100 / len(questions_and_answers), "%")
        print("You get ", correct * 10 / len(questions_and_answers), " out of 10")
    else:
        print("Unfortunately you did not answer any question correctly")
        print("0% correct answers")
        print("You get 0 points")
    # I store the results in my empty dictionary, so in the end to show a statistic about average of users
    # If the numbers of right answers are already store in my dictionary, I will add just the name of person who score
    # otherwise I create a new key with the corresponding to the number of correctly answered questions, and add the name of person to that key
    if correct in quiz_results:
        quiz_results[correct] += " " + name
    else:
        quiz_results[correct] = name
    average_score += correct * 100 / len(questions_and_answers)


# continue_value is default "y" (yes) for the first user and also the "players" variable is default 1
continue_value = 'y'
players = 1
# I will repeat everything for each user, until no users left
while (continue_value == "y"):
    # I call the quiz function
    quiz(player_name)
    # After the function is finish I check if anybody want to take the quiz
    continue_value = input("Does anybody else want to take the quiz?y/n ")
    # I keep asking until I get a "y"(yes) or "n"(no) using the while loop
    while (continue_value != "y" and continue_value != "n"):
        continue_value = input("Please input a valid value! y/n ")
    if (continue_value == 'y'):
        # If the answer is "y"(yes) than we input the player_name, increment the players number, and shuffle the questions
        player_name = input("Please enter your name: ")
        players += 1
        temporary_list = list(questions_and_answers.items())
        random.shuffle(temporary_list)
        questions_and_answers = dict(temporary_list)
        # After this, the loop will go back for give the quiz to the new player
# to be able to order the quiz results I use an OrderDict
ordered_results = collections.OrderedDict(sorted(quiz_results.items()))
quiz_results = ordered_results
# to be able to show the last element (the user with the biggest score) I put my quiz_results into a list and accesed the last element with indix -1
results_list = list(quiz_results.items())
# In the end I print the general statistics
# The one/s with the biggest grades will always be the first in my sorted by key dictionary
print("The user/s with the biggest score is:", results_list[-1])
# To print all the scores, I print the whole dictionary
print("Here you can see all the users scores:", results_list)
# To calculate the average score, I divide all players added score to players number
print("The average score of all of the users is: ", average_score / players, "%")
