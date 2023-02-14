"""Function printing python version."""
import random
import math
import os
from hangman_words import alphabet
from hangman_art import LOGO2
from hangman_art import GAVEL
from hangman_art import TREASURE
from hangman_art import CALCULATOR
from hangman_art import BLACKJACK

# #String length ------------------------------------->
# print(len(input("What is your name? \n")))

# name = input("What is your name? ")
# length = len(name)
# print(length)

# #Band Name Generator ------------------------------------->
# city = input("What is the name of the city you grew up in?\n")

# pet = input("What's your pets name?\n")

# bandname = print(city + pet)

# #Adding 2 numbers from same input ------------------------------------->
# two_digit_number = input("Type a two digit number: \n")

# print(int(two_digit_number[0]) + int(two_digit_number[1]))


# #BMI Calculator ------------------------------------->
# height = input("enter your height in m: \n")
# weight = input("enter your weight in kg: \n")

# print(int(int(weight) / (float(height) ** 2)))

# #Rouding numbers ------------------------------------->
# #Number after , is the place we want to round to.
# print(round(8/3, 2))


# #Days, Weeks, Months, left to live------------------------------------->
# age = input("What is your current age? \n")

# Years = (90 - int(age))
# months = (Years * 12)
# weeks = (Years * 52)
# days = (Years * 365)


# print("You have " + str(days) + " days, " + str(weeks) + " weeks, " + "and " + str(months) + " months left.\n")
# print(f'You have " + {days} + " days, " + {weeks} + " weeks, " + "and " + {months} + " months left.\n')

#  #Tip Calculator ------------------------------------->
# print("Welcome to the tip calculator!")
# bill = float( input( "What was the total bill? \n$"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
# people = int(input("How many people to split the bill?\n"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(final_amount)

# # If else Statement ------------------------------------->
# NUMBER = int(float(input("Which number do you want to check? \n")))
# if NUMBER % 2 == 0:
#     print("This is an even number.\n")
# else:
#     print("This is an odd number.\n")

# #BMI Checker(if/elif) ------------------------------------->
# height = float(input("enter your height in m: \n"))
# weight = float(input("enter your weight in kg: \n"))
# # 🚨 Don't change the code above 👆
# BMI = round(weight / height ** 2)
# if BMI <= 18.5:
#     print(f"Your BMI is {BMI}, you are under weight.")
# elif BMI <= 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI <= 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI <= 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# elif BMI > 35:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

# # Leap year checker ------------------------------------->
# year = int(input("Which year do you want to check? \n"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# #Pizza ordering ------------------------------------->
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n")
# add_pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# BILL = 0

# if size == ("S", "s"):
#     BILL += 15
# elif size == ("M","m"):
#     BILL += 20
# elif size == ("L","l"):
#     BILL += 25

# if add_pepperoni == ("Y", "y"):
#     if size == ("S","s"):
#         BILL += 2
#     else:
#         BILL += 3

# if extra_cheese == ("Y","y"):
#     BILL += 1

# print(f"Your final bill is ${BILL}")

# # Love Calculator ------------------------------------->
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1.lower() + name2.lower()

# t = combined_string.count("t")
# r = combined_string.count("r")
# u = combined_string.count("u")
# e = combined_string.count("e")

# true = t + r + u + e

# l = combined_string.count("l")
# o = combined_string.count("o")
# v = combined_string.count("v")
# e = combined_string.count("e")

# love = l + o + v + e

# LOVE_SCORE = int(str(true) + str(love))

# if (LOVE_SCORE < 10) or (LOVE_SCORE > 90):
#     print(f"Your love score is {LOVE_SCORE}, you go together like coke and mentos")
# elif (LOVE_SCORE >= 40) and (LOVE_SCORE <= 50):
#     print(f"Your score is {LOVE_SCORE}, you are alright together.")
# else:
#     print(f"Your score is {LOVE_SCORE}")

# print(LOVE_SCORE)


# #Treasure Game ------------------------------------->
# print(TREASURE)
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# choice1 = input('You\'re at a crossroad,' +
#                 'where do you want to go? Type "left" or "right".\n').lower()
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake,' +
#                     'there is a island in the middle of the lake.' +
#                     'Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
#     if choice2 == "wait":
#         choice3 = input('You arrive at the island unharmed.' +
#                         'There is a house with 3 doors.' +
#                         'One red, one yellow, one blue. Which color do you choose?\n').lower()
#         if choice3 == "red":
#             print("it\'s a room full of fire. Game Over!")
#         elif choice3 == "yellow":
#             print("You found the treasure, You Win!")
#         elif choice3 == "blue":
#             print("It's a room full of beasts. Game Over!")
#         else:
#             print("You choose a door that doesn\'t exist. Game Over!")
#     else:
#         print("You got attacked by an agry trout. Game Over")
# else:
#     print("You fell into a hole. Game Over.")


# #Heads or Tails ------------------------------------->

# random_num = random.randint(0,1)
# if random_num == 1:
#     print("Heads")
# else:
#     print("Tails")

# #Random name picker ------------------------------------->
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# num_items = len(names)

# random_choice = random.randint(0, num_items -1)

# person = names[random_choice]

# print(f"{person} is going to buy the meal today!")

# #X marks the spot------------------------------------->
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# H_Position = int(position[0])
# V_Position = int(position[1])

# selected_row = map[V_Position - 1]
# selected_row[H_Position - 1] = "X"
# #Simpler version of above............
# map[V_Position - 1][H_Position - 1] = "X"


# print(f"{row1}\n{row2}\n{row3}")

# #Rock, Paper, Scissors ------------------------------------->

# ROCK = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# PAPER = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# SCISSORS = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [ROCK, PAPER, SCISSORS]

# user_choice = int(input("What do you choose? Type 0 fo Rock, 1 for Paper, or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed and invalid number! You Lose!")
# else:
#     print(game_images[user_choice])

# computer_choice = random.randint(0,2)
# print("Computer chose:")
# print(game_images[computer_choice])


# if user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif computer_choice == user_choice:
#     print("it's a draw!")


# #LOOPS ----------------------------------------------->
# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

# # Average Height using For Loops ---------------------------------------->
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# TOTAL_HEIGHT = 0
# for height in student_heights:
#     TOTAL_HEIGHT += height

# TOTAL_STUDENTS = 0
# for student in student_heights:
#     TOTAL_STUDENTS += 1

# average = round(TOTAL_HEIGHT / TOTAL_STUDENTS)
# print(average)

# #Highest Score ---------------------------------->
# student_scores = input("Input a list of student scores ").split()

# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# HIGH_SCORE = 0
# for score in student_scores:
#     if score > HIGH_SCORE:
#         HIGH_SCORE = score
# print(f"The highest score in the class is: {HIGH_SCORE}")

# #Calculate total of all even numbers 1 to 100------------------------->
# TOTAL = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         TOTAL += number
# print(TOTAL)
# #SAME AS ABOVE------>
# TOTAL = 0
# for number in range(2, 101, 2):
#     TOTAL += number
# print(TOTAL)

# #FIZZBUZZ -------------------------------------------------------------->
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 ==0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# #Random Password Generator ------------------------------------------->
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))

# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
# random.shuffle(password_list)
# print(password_list)

# PASSWORD = ""
# for char in password_list:
#     PASSWORD += char
# print(f"Your password is: {PASSWORD}")

# #Hangman Game ----------------------------------------------------------------->
# from hangman_art import stages, LOGO
# from hangman_words import WORD_LIST

# LIVES = 6


# chosen_word = random.choice(WORD_LIST)
# print(LOGO)
# DISPLAY = []

# for letter in range(len(chosen_word)):
#     DISPLAY += "_"


# END_OF_GAME = False

# while not END_OF_GAME:
#     #Take users input and lowercase it
#     guess = input("Guess a letter:\n").lower()

#     #Clears the screen after every guess
#     clear()

#     #check if letter has already been guessed
#     if guess in DISPLAY:
#         print(f"You've already guess {guess}")

#     #Loop through the length of the choosen word
#     for position in range(len(chosen_word)):
#         #Asign each letter a position in the array
#         letter = chosen_word[position]
#         #If the guess is there asign the guess to that position
#         if letter == guess:
#             DISPLAY[position] = letter

#     #If the guess is not there, subtract a life,
#     # if there are no more lives end the game and print the correct word.
#     if guess not in chosen_word:
#         print(f"You guessed {guess},that's not in the word. You lose a life!")
#         LIVES -=1
#         if LIVES == 0:
#             END_OF_GAME = True
#             print("You Lose")
#             print(f"The word was {chosen_word}")

#     print(f"{' '.join(DISPLAY)}")

#     #If there are no more dashes end game and print you win!
#     if "_" not in DISPLAY:
#         END_OF_GAME = True
#         print("You Win!!")
#     #print the ASCII art and the number of lives
#     print(stages[LIVES])

# #Function that allows for input
# def greet_with_name(name):
#     """Function printing python version."""
#     print(f"Hello {name}")

# greet_with_name("Rodrigo")

# # Area of a wall------------------------------------------------------>
# def paint_calc(height, width, cover):
#     """Function printing python version."""
#     num_of_cans = (height * width) / cover
#     round_up_cans = math.ceil(num_of_cans)
#     print(f"You'll need {round_up_cans} cans of paint")

#     test_h = int(input("Height of wall: "))
#     test_w = int(input("Width of wall: "))
#     coverage = 5
#     paint_calc(height=test_h, width=test_w, cover=coverage)

# paint_calc(5,5,5)

# #Prime number checker -------------------------------------------------->
# def prime_checker(number):
#     """Function printing python version."""
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# #Caeser Cypher -------------------------------------------------------------->
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# shift = shift % 26

# def encrypt(plain_text, shift_amount):
#     """Function printing python version."""
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     """Function printing python version."""
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

# print(LOGO2)

# def caeser(start_text, shift_amount, cipher_direction):
#     """Function printing python version."""
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"The {cipher_direction}d result: {end_text}")
#     print("")

# SHOULD_CONTINUE = True
# while SHOULD_CONTINUE:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     shift = shift % 26
#     caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
#     result = input("Type yes' if you want to go again. Otherwise type 'no'.\n")
#     if result == "no":
#         SHOULD_CONTINUE = False
#         print("GoodBye!")

# #Python Dictionaries------------------------------------->
# #Create Dictionary with key value pairs........
# programming_dictionary = {
#     "Bug": "An error in a program that orevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again",
#     "Loop": "The action of doing something over and over again."
# }
# # Retrieve items from dictionary..........

# print(programming_dictionary["Function"])

# empty_dictionary = {}

# empty_dictionary["Name"] = "Rodrigo"
# print(empty_dictionary)

# #Looping through a dictionary --------------------->
# names = {
#     "first_name": "Rodrigo",
#     "second_name": "Ricardo",
#     "third_name": "David"
# }
# for name in names:
#     print(name) #Gives Key
#     print(names["first_name"]) #Gives Value

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades ={}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 91:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     elif score > 70:
#         student_grades[student] = "Fail"    

# print(student_grades)

# #Nesting Dictionaries------------------>
# capitals = {
#     "France":"Paris",
#     "Germany":"Berlin",
# }
# #Dictionary within Dictionary, list value, int value
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits: ": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits: ": 5}
# }
# #Dictionary within a list
# travel_log = [
#     {
#         "country": "France",
#         "visits: ": 12,
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#         },
#     {
#         "country": "Germany",
#         "visits: ": 5,
#         "cities_visited": ["Berlin",
#         "Hamburg", "Stuttgart"]
#         }
# ]

# def add_new_country(country, vists, cities_visted):
#     """Function printing python version."""
#     new_country = {}
#     new_country["country"] = country
#     new_country["vists"] = vists
#     new_country["cities_visted"] = cities_visted
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# #Silent Bid------------------------------------------------------->
# print("Welcome to the secret auction project.")
# print(GAVEL)
# bids = {}
# BIDDING_FINISHED = False

# def find_highest_bidder(bidding_record):
#     """Function printing python version."""
#     highest_bid = 0
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of {highest_bid}")

# while not BIDDING_FINISHED:
#     name = input("What is your name?: ")
#     bid = int(input("What is your bid?: $"))
#     bids[name] = bid
#     should_continue = input("Are there any other bidders? 'yes or 'no. ")
#     if should_continue == "no":
#         BIDDING_FINISHED = True
#     elif should_continue == "yes":
#         os.system('clear')

# find_highest_bidder(bids)

# #Functions with Outputs---------------------------------------------->
# def format_name(f_name,l_name):
#     """Function printing python version."""
#     full_name = f_name.title() +", "+ l_name.title()
#     return f"{full_name}"

# formatted_String = format_name("rodrigo", "marquez")
# print(formatted_String)
# print(format_name("rodrigo", "marquez"))

# print(format_name(input("What is your first name?"),input("What's your last name? ")))

# # Leap year and month checker ------------------------------------->
# def is_leap(year):
#     """Function printing python version."""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 ==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     """Checks year for leap and month for number of days."""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# #Calculator App--------------------------------------->
# #Add
# def add(n_one, n_two):
#     """Add"""
#     return n_one + n_two
# #Subtract
# def subtract(n_one, n_two):
#     """Subtract"""
#     return n_one - n_two
# #Multiply
# def multiply(n_one, n_two):
#     """Multiply"""
#     return n_one * n_two
# #Divide
# def divide(n_one, n_two):
#     """Divide"""
#     return n_one / n_two

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator():
#     """Calculator app"""
#     print(CALCULATOR)
#     num1 = float(input("Whats the first number?: "))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("Whats the next number?: "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ") == "y":
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()

# calculator()

#BlackJack----------------------------------------------------------------------->

print(BLACKJACK)
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#Create 2 empty lists for each player----------->
user_cards = []
computer_cards = []
IS_GAME_OVER = False

#Return 2 random cards---------------->
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or computer_score == 0 or user_score > 21:
    IS_GAME_OVER = True
