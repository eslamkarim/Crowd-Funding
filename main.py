import os
from register import register
from login import login

def main_screen():
    print("Welcome to Crowd Funding")
    user_input = input("Please pick an option:\n1)Login  \n2)Register\n3)Exit\n")
    if user_input == "1" or user_input.lower() == "login":
        os.system("cls")
        login()
    elif user_input == "2" or user_input.lower() == "register":
        os.system("cls")
        register()
        main_screen()
    elif user_input == "3" or user_input.lower() == "exit":
        os.system("cls")
        print("Thank you for using crowd funding")
        exit()
    else:
        os.system("cls")
        print("Wrong choice")
        main_screen()
        

os.system("cls")
main_screen()