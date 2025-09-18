#!/usr/bin/python3

"""
Program name: guessnumber.py
Program Purpose: A simple number guessing game.
Author: Kyle vachon
Date and Version: 2024-06-15 v1.0
Completion time: 15 minutes
"""

import random

secret = random.randint(1, 9)
guessed_number = int(input("Welcome to the number guessing game!\nGuess a number from 1 - 9. (0 to quit)"))

# Main loop for the guessing game
while guessed_number != secret and guessed_number != 0:
    if guessed_number < 0 or guessed_number > 9:
        guessed_number= int(input("Invalid input. Please guess a number between 1 and 9."))
    elif guessed_number < secret:
        print("Your guess is too low: guess higher.")
        guessed_number = int(input("Guess again from 1-9 (0 to quit): "))
    elif guessed_number > secret:
        print("Your guess is too high: guess lower.")
        guessed_number = int(input("Guess again from 1-9 (0 to quit): "))

#Exit statement checking if you guessed correctly or quit
if guessed_number == secret:
    print("Congratulation:", guessed_number, "is a match. You win!")
else: 
    print("Thanks for playing! Goodbye.")


