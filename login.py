import re
from projects import project_main_screen
import datetime

def login():
    email = ""
    password = ""
    users_read = open("users.txt",'r')

    while not re.match("^[A-Za-z_\-0-9]+@[A-Za-z]+\.[a-z]+$",email): #must be valid email
        email = input("Enter your email\n")
        password = input("Enter your password:\n")
        users_read.seek(0,0)
        for user_dict in users_read.read().splitlines():
            if eval(user_dict)['email'] == email and eval(user_dict)['password'] == password:
                print("logged in")
                users_read.close()
                project_main_screen(user_dict)
                break
        else:
            print("Wrong email or password")
            email = ""
            password = ""
    