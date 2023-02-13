# """Function printing python version."""
# import random
# import math
# from hangman_words import alphabet
# from hangman_art import LOGO2
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
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake, there is a island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
#     if choice2 == "wait":
#         choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n').lower()
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
# from replit import clear
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
#     #If the guess is not there, subtract a life, if there are no more lives end the game and print the correct word.
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

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades ={}

for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    elif score > 70:
        student_grades[student] = "Fail"    

print(student_grades)
