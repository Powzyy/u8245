#!/usr/bin/python3

"""
Program name: exponentiate.py
Program Purpose: This program prompts the user for a number and then returns the square and cube of that number.
Author: Kyle vachon
Date and Version: 2024-06-25 v1.0
Completion time: 30 minutes
"""

##functions
#prompt user for a number and returns it as an integer
def get_integer():
    user_input = input("Please enter a number (q to quit): ")
    if user_input.lower() == "q":
        return "q"
    return int(user_input)

#takes in a number and returns the square of that number
def square(number):
    squared_number = number*number
    return squared_number

#takes in a number and returns the cube of that number 
def cube(number):
    cubed_number=number*number*number
    return cubed_number

#main
proceed = input("This program squares and cubes numbers.\nWould you like to proceed? (y to proceed, q to quit): ")
while proceed.lower() == "y" and proceed.lower() != "q":
    chosen_number = get_integer()
    if chosen_number == "q":
        proceed = "q"
    elif chosen_number == 0:
        print("The square of", 0, "is", 0, "and the cube is", 0)
    elif chosen_number == 1:
        print("The square of", 1, "is", 1, "and the cube is", 1)
    else:
        squared_chosen_number = square(chosen_number)
        cubed_chosen_number = cube(chosen_number)
        print("The square of", chosen_number, "is", squared_chosen_number, "and the cube is", cubed_chosen_number)

#Closing message
print ("Thank you for using this program. Goodbye!")
