import random
import math

min_threshold = 0
max_threshold = 10


# generates user prompt
def user_prompt():
    print('''
    Enter the number of the type of arithmetic problem you want to practice.
    1) Addition 2) Subtraction 3) Exponential Function 4) Pythagorean Theorem
    ''')


# user inputs how many questions they want to practice
def num_of_questions():
    while True:
        try:
            total_problems = int(input("How many questions do you want to practice? "))
        except ValueError:
            print("Please enter a number")
        else:
            return total_problems


def user_choice():
    while True:
        try:
            user_input = int(input("Your choice: "))
        except ValueError:
            print("Please enter a number to select what type of math questions you want to practice.")
        else:
            return user_input


# generates random numbers from 0 to 10
def generate_input():
    return random.randint(min_threshold, max_threshold)


# generate math question based on user selection
def create_arithmetic_problem_prompt(a, b, user_input):
    if user_input == 1:
        user_input = '+'
        print("What is " + str(a) + " " + str(user_input) + " " + str(b) + "?")
    elif user_input == 2:
        user_input = '-'
        print("What is " + str(a) + " " + str(user_input) + " " + str(b) + "?")
    elif user_input == 3:
        print("What is " + str(a) + " to the power of " + str(b) + " ?")
    elif user_input == 4:
        print("What does " + (str(a)) + " squared + " + str(b) + " squared make c, the hypotenuse ?")


# addition
def addition(a, b):
    return a + b


# subtraction
def subtraction(a, b):
    return a - b


# exponential
def exponential(a, b):
    return a ** b


# pythagorean
def pythagorean(a, b):
    return math.sqrt(a ** 2 + b ** 2)


# this function ensures user only input numbers
def validate_user_answer():
    while True:
        try:
            user_answer = int(input("Your answer is: "))
        except ValueError:
            print("Bad Input! Please enter your answer in numbers.")
        else:
            return user_answer


# compare user answer and the true answer based on their chosen operation
def check_answer(user_input, a, b, user_answer):
    num_correct = 0
    problems_solved = 0
    if user_input == 1:
        if addition(a, b) == user_answer:
            print('Correct!')
            return True
        else:
            print("Incorrect. The expected answer was " + str(addition(a, b)))
            return False
    elif user_input == 2:
        if subtraction(a, b) == user_answer:
            print('Correct!')
            return True
        else:
            print("Incorrect. The expected answer was " + str(subtraction(a, b)))
            return False
    elif user_input == 3:
        if exponential(a, b) == user_answer:
            print('Correct!')
            return True
        else:
            print("Incorrect. The expected answer was " + str(exponential(a, b)))
            return False
    elif user_input == 4:
        if pythagorean(a, b) == user_answer:
            print('Correct!')
            return True
        else:
            print("Incorrect. The expected answer was " + str(pythagorean(a, b)))
            return False


def main():
    num_correct = 0  # initiate counter
    problem_solved = 0  # initiate counter
    for x in range(num_of_questions()):
        (user_prompt())
        user_input = user_choice()
        a = generate_input()
        b = generate_input()
        create_arithmetic_problem_prompt(a, b, user_input)
        user_answer = validate_user_answer()
        if not check_answer(user_input, a, b, user_answer):
            problem_solved += 1
        else:
            num_correct += 1
            problem_solved += 1
            print("You got", num_correct, "out of", problem_solved, "questions correct.")

    print("Your score is", num_correct / problem_solved * 100,"%")


if __name__ == "__main__":
    main()
