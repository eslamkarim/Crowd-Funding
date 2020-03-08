import os
import re
import datetime

def project_main_screen(email):
    os.system("cls")
    print(email)
    user_input = input("Please pick an option:\n1)Create a project  \n2)View Projects\n3)Exit\n")
    if user_input == "1" or user_input.lower() == "create":
        os.system("cls")
        create_project(email)
    elif user_input == "2" or user_input.lower() == "view":
        os.system("cls")
        pass
        #view_all_projects()

def create_project(email):
    project = {}
    fl = open("projects.txt", 'a')
    projects_read = open("projects.txt", 'r')
    project_title = ""
    while not re.match("^[A-Za-z ]+$",project_title): #must be valid email
        project_title = input("Enter the project title:\n")
        projects_read.seek(0,0)
        for project_dict in projects_read.read().splitlines():
            if eval(project_dict)['title'] == email:
                print(project_dict)
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

    print(project)
