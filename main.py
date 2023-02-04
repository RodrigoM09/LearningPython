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
