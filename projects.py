import os
import re
import datetime
import fileinput

def project_main_screen(user_dict):
    os.system("cls")
    print(user_dict)
    user_input = input("Please pick an option:\n1)Create a project  \n2)View Projects\n3)Exit\n")
    if user_input == "1" or user_input.lower() == "create":
        os.system("cls")
        create_project(user_dict)
    elif user_input == "2" or user_input.lower() == "view":
        os.system("cls")
        pass
        #view_all_projects()
    elif user_input == "3" or user_input.lower() == "exit":
        os.system("cls")
        print("Thank you for using crowd funding")
        exit()
    else:
        os.system("cls")
        print("Wrong choice")
        project_main_screen()

def create_project(user_dict):
    project = {}
    user_projects = eval(user_dict)["projects"]
    project_title = ""
    while not re.match("^[A-Za-z ]+$",project_title): #must be valid email
        project_title = input("Enter the project title:\n")
        for pr in user_projects:
            if pr['title'] == project_title:
                print(pr)
                print("project title exists")
                project_title = ""
                break
    project['title'] = project_title
    
    project_details = ""
    while not re.match("^[A-Za-z ]+$",project_details):
        project_details = input("Please enter valid details:\n")
    project['details'] = project_details
    
    project_target = ""
    while not re.match("^[0-9]+$",project_target):
        project_target = input("Please enter valid target:\n")
    project['target'] = project_target
    
    while True:
        start_date = input("Please enter valid date YYYY-MM-DD:\n")
        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
        else:
            break
    project['start_date'] = start_date

    l= eval(user_dict)["projects"][:]
    l.append(project)
    d= eval(user_dict)
    d["projects"] = l[:]
    print(d)
    edit_project(d)
    project_main_screen(str(d))

def edit_project(user_dict):
    for line in fileinput.FileInput("users.txt", inplace=True):
        if eval(line)['email'] == user_dict['email']:
            print(user_dict)
        else:
            print(line)
    fileinput.close()            