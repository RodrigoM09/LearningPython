#String length ------------->
print(len(input("What is your name? ")))

name = input("What is your name? ")
length = len(name)
print(length)

#Band Name Generator --------->
city = input("What is the name of the city you grew up in?\n")

pet = input("What's your pets name?\n")

bandname = print(city + pet)

#Adding 2 numbers from same input ------>
two_digit_number = input("Type a two digit number: ")

print(int(two_digit_number[0]) + int(two_digit_number[1]))


#BMI Calculator --------->
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print(int(int(weight) / (float(height) ** 2)))

#Rouding numbers ------->
#Number after , is the place we want to round to.
print(round(8/3, 2))


#Days, Weeks, Months, left to live--------->
age = input("What is your current age? ")

Years = (90 - int(age))
months = (Years * 12)
weeks = (Years * 52)
days = (Years * 365)


print("You have " + str(days) + " days, " + str(weeks) + " weeks, " + "and " + str(months) + " months left.")
print(f"You have " + {days} + " days, " + {weeks} + " weeks, " + "and " + {months} + " months left.")
 

 #Tip Calculator --------->
print("Welcome to the tip calculator!")
bill = float( input( "What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(final_amount)

# If else Statement ----------->
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#BMI Checker(if/elif) ------->
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
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