#!/usr/bin/python3

"""
Program name: guess_course.py
Program purpose: guess the course code with a while loop
Author: Kyle Vachon
Date and Version: 09/11/2025 v1.0
Completion time: 20 minutes
"""

#variables
course_code = "CST8245"
guessed_code = "" # initialize guessed_code to an empty string

# while loop that keeps going until the user guesses right or chooses to exit 
while guessed_code != course_code:
    #prompt user for input
    guessed_code = input("Press q to exit ,or Guess the course code (e.g., CST1000): ")

    #if the user wants to exit then print exit message and exit the while loop
    if guessed_code == "q":  
        print("Exiting the program.")
        break
    #if the guess is wrong then print incorrect message and itterate the while loop
    elif course_code != guessed_code:
        print("Incorrect course code. Please try again.")
    #if the guess is right then print correct message and exit the while loop
    elif guessed_code == course_code:
        print("Congratulations! You guessed the correct course code.")

#end of program message
print("Thank you for playing!")









