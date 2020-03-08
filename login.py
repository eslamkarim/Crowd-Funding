import re
from projects import project_main_screen

def login():
    email = ""
    users_read = open("users.txt",'r')

    while not re.match("^[A-Za-z_\-0-9]+@[A-Za-z]+\.[a-z]+$",email): #must be valid email
        email = input("Enter your email\n")
        users_read.seek(0,0)
        for user_dict in users_read.read().splitlines():
            if eval(user_dict)['email'] == email:
                break
        else:
            email = ""


    password = ""
    while not re.match("^[A-Za-z0-9]{8}$",password):
        password = input("Enter your password:\n")
        users_read.seek(0,0)
        for user_dict in users_read.read().splitlines():
            if eval(user_dict)['password'] == password:
                print("logged in")
                project_main_screen(email)
                break
        else:
            password = ""
    