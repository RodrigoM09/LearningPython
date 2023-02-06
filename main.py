#String length ------------------------------------->
print(len(input("What is your name? \n")))

name = input("What is your name? ")
length = len(name)
print(length)

#Band Name Generator ------------------------------------->
city = input("What is the name of the city you grew up in?\n")

pet = input("What's your pets name?\n")

bandname = print(city + pet)

#Adding 2 numbers from same input ------------------------------------->
two_digit_number = input("Type a two digit number: \n")

print(int(two_digit_number[0]) + int(two_digit_number[1]))


#BMI Calculator ------------------------------------->
height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")

print(int(int(weight) / (float(height) ** 2)))

#Rouding numbers ------------------------------------->
#Number after , is the place we want to round to.
print(round(8/3, 2))


#Days, Weeks, Months, left to live------------------------------------->
age = input("What is your current age? \n")

Years = (90 - int(age))
months = (Years * 12)
weeks = (Years * 52)
days = (Years * 365)


print("You have " + str(days) + " days, " + str(weeks) + " weeks, " + "and " + str(months) + " months left.\n")
print(f'You have " + {days} + " days, " + {weeks} + " weeks, " + "and " + {months} + " months left.\n')
 

 #Tip Calculator ------------------------------------->
print("Welcome to the tip calculator!")
bill = float( input( "What was the total bill? \n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(final_amount)

# If else Statement ------------------------------------->
number = int(float(input("Which number do you want to check? \n")))
if number % 2 == 0:
    print("This is an even number.\n")
else:
    print("This is an odd number.\n")

#BMI Checker(if/elif) ------------------------------------->
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆
BMI = round(weight / height ** 2)
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are under weight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")

# Leap year checker ------------------------------------->
year = int(input("Which year do you want to check? \n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not a leap year.")    
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#Pizza ordering ------------------------------------->
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or  size == "l":
    bill += 25 

if add_pepperoni == "Y" or  add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3 

if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1

print(f"Your final bill is ${bill}")

# Love Calculator ------------------------------------->
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1.lower() + name2.lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

print(love_score)


#Treasure Game ------------------------------------->
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is a island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n').lower()
        if choice3 == "red":
            print("it\'s a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure, You Win!")
        elif choice3 == "blue":
            print("It's a room full of beasts. Game Over!")
        else:
            print("You choose a door that doesn\'t exist. Game Over!")
    else:
        print("You got attacked by an agry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")


#Heads or Tails ------------------------------------->
import random 

random_num = random.randint(0,1)
if random_num == 1:
    print("Heads")
else:
    print("Tails")

#Random name picker ------------------------------------->
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1)

person = names[random_choice]

print(f"{person} is going to buy the meal today!")

#X marks the spot------------------------------------->
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

H_Position = int(position[0])
V_Position = int(position[1])

selected_row = map[V_Position - 1]
selected_row[H_Position - 1] = "X"
#Simpler version of above............
map[V_Position - 1][H_Position - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")

#Rock, Paper, Scissors ------------------------------------->
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 fo Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed and invalid number! You Lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("it's a draw!")



