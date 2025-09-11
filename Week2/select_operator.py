#!/usr/bin/python3

"""
Program_Name: select_operator.py
Program_Purpose: Demonstrate the use of the if, elif and else selection statements
Author: Kyle Vachon
Date and Version: 20215/09/10 ver 1.0
Completion Time: 10 minutes
"""

operator = input("Please choose one of four arithmetic operators(+,-,* or /): ")

# + operator selected
if  operator == "+":
    print("You have chosen addition")
# - operator selected
elif operator == "-":
    print("You have chosen subtraction")
# * operator selected    
elif operator == "*":
    print("You have chosen multiplication")
# / operator selected  
elif operator == "/":
    print("You have chosen division")
# invalid operator selected
else:
    print("You have not chosen a valid operator")

# End of program
print("Thank you for using this program")
