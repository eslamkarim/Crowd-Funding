import os
import re
import datetime
import fileinput

def project_main_screen(user_dict):
    os.system("cls")
    print(user_dict)
    user_input = input("Please pick an option:\n1)Create a project  \n2)View Projects\n3)Update Project\n4)Delete project\n5)Exit\n")
    if user_input == "1" or user_input.lower() == "create":
        os.system("cls")
        create_project(user_dict)
    elif user_input == "2" or user_input.lower() == "view":
        os.system("cls")
        view_all_projects(user_dict)
    elif user_input == "3" or user_input.lower() == "update":
        os.system("cls")
        update_project_details(user_dict)
        project_main_screen(user_dict)
    elif user_input == "4" or user_input.lower() == "delete":
        os.system("cls")
        delete_project(user_dict)
    elif user_input == "5" or user_input.lower() == "exit":
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
        start_date = input("Please enter valid start date YYYY-MM-DD:\n")
        try:
            start_date=datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            if start_date < datetime.date.today():
                raise ArithmeticError()
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
        except ArithmeticError:
            print("The date must be on or after today")
        else:
            break
    project['start_date'] = start_date
    
    while True:
        end_date = input("Please enter valid end date YYYY-MM-DD:\n")
        try:
            end_date=datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            if start_date > end_date:
                raise ArithmeticError()
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
        except ArithmeticError:
            print("The date must be on or after start date")
        else:
            break
    project['end_date'] = end_date

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
            print(str(user_dict))
        else:
            print(str(line),end="")
    fileinput.close()            

def view_all_projects(user_dict):
    os.system("cls")
    print("Your projects---------->")
    projects_list = eval(user_dict)['projects']
    for project in projects_list:
        print(F"Title: {project['title']}\n   Details: {project['details']}\n   Target: {project['target']}$\n   Start Date: {project['start_date']}\n   End Date: {project['end_date']}\n")
    input("Press Enter to continue...")
    project_main_screen(user_dict)

def update_project_details(user_dict):
    os.system("cls")
    i = 0
    project_title = ""
    update_key=""
    user_projects = eval(user_dict)['projects']
    while not re.match("^[A-Za-z ]+$",project_title): #must be valid email
        project_title =  input("Enter project title to edit\n")
        for pr in user_projects:
            if pr['title'] == project_title:
                while not re.match("^[A-Za-z_]+$",update_key): #must be valid email
                    update_key = input("please insert the key you want to update\n")
                    if update_key not in pr.keys():
                        print("Key doesn't exist")
                        update_key = ""
                update_value = input("insert your update\n")
                pr.update({update_key : update_value})
                x=eval(user_dict)
                x['projects'][i]=pr
                edit_project(x)
                i=0
                break
            i += 1
        else:
            print("project doesn't exist")
            project_title=""
            i = 0   
def delete_project(user_dict):
    os.system("cls")
    project_title = ""
    x=eval(user_dict)
    user_projects = eval(user_dict)['projects']
    new_user_projects = []
    while not re.match("^[A-Za-z ]+$",project_title): #must be valid email
        project_title =  input("Enter project title to edit\n")
        for pr in user_projects:
            if pr['title'] == project_title:
                continue
            else:
                new_user_projects.append(pr)
    x["projects"] = new_user_projects
    edit_project(x)
