#!/usr/bin/python3

"""
Program name: calc_sequential.py
Program purpose: 
Author: Kyle Vachon, vach0111, 013
Date and version: September 5th 2025, ver1.0
Completion time: 20 Minutes
"""

#Greet the user
user_name=input("Please enter your nanme: ")
print("Hello " + user_name + "!")

#Prompting for user input
operand_one = input("Please enter an Operand: ")
operand_one = float(operand_one)
operand_two = input("Please enter another Operand: ")
operand_two = float(operand_two)

#Perform aritmetic calculation and display results
sum = operand_one + operand_two
diff = operand_one - operand_two
print(f"Result of addition as float: ", sum, " as int :", int(sum))
print(f"Result of subtraction as float: ", diff, " as int: ", int(diff))

#Close the program
print("Thank you ", user_name)