import re
import os

def register():
    user = {}
    print("You are now registering you need to provide First Name, Last Name, Email, Password and a phone number")
    
    fl = open("users.txt", 'a')
    users_read = open("users.txt",'r')
    fname = input("Enter the first name:\n")
    while not re.match("^[A-Za-z]+$",fname): #must be only string with no spaces
        fname = input("Please enter valid first name:\n")
    user["fname"] = fname

    lname = input("Enter the last name:\n") #must be only string with no spaces
    while not re.match("^[A-Za-z]+$",lname):
        lname = input("Please enter valid last name:\n")
    user["lname"] = lname

    email = ""
    while not re.match("^[A-Za-z_\-0-9]+@[A-Za-z]+\.[a-z]+$",email): #must be valid email
        email = input("Enter the email:\n")
        users_read.seek(0,0)
        for user_dict in users_read.read().splitlines():
            if eval(user_dict)['email'] == email:
                print(user_dict)
                print("Email exists")
                email = ""
                break
    user["email"] = email

    password = input("Enter the password:\n")
    while not re.match("^[A-Za-z0-9]{8,}$",password):
        password = input("Please enter valid password must be at least 8 characters long:\n")

    matching_password = input("Enter password again:\n")
    while password != matching_password:
        matching_password = input("Passwords don't match try again:\n")
    user["password"] = password

    phone = input("Enter phone number:\n")
    while not re.match("^01[0125][0-9]{8}$",phone): #must be only string with no spaces
        phone = input("Please enter valid phone number:\n")
    user["phone"] = phone

    fl = open("users.txt", 'a')
    fl.write(str(user))
    fl.write("\n")
    fl.close()
    users_read.close
    os.system("cls")

