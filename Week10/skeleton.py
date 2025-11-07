#!/usr/bin/python3

"""
Program name: skeleton.py
Program Purpose: Skeleton program for a book database
Author: Kyle vachon
Date and Version: 2025-11-06 v1.0
Completion time: 
"""

#variables
option = ''

##functions
#show the menu
def show_menu():
    print ("1. Add a new book" )
    print ("2. View all books" )
    print ("Q. Quit" )

#select a menu option and have it returned
def get_menu_option(prompt):
    return input(prompt).strip()

#select an attribute and have it returned
def get_attribute_value(prompt):
    return input(prompt).strip()


#main
while option != 'Q':
    show_menu()
    option = get_menu_option("Select an option: ").upper()
    if option == '1':
        print("You selected option 1: add a new book")
    elif option == '2':
        print("You selected option 2: view all books")
    elif option == 'Q':
        print("Quitting the program.")
    else:
        print("Invalid option, please try again.")