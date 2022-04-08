#This is my string concatination practice
#print("Day 1 - String Manipulation")
#print('String Concatenation is done with the "+" sign.')
#print('e.g. print("Hello " + "world")')
#print("New lines can be created with a backslash and n.")

#Here I have use len function with str to print the input length of name characters
# print("Your name has " + str(len(input("What is your name? "))) + " characters in it")


# The code below is swapping the VARIABLES ouput
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#Here I have solved a simple basic challenge which was given at the end of Day 1 where it has asked to create a band name. 

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be " + city + " " +  pet_name)
#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.
