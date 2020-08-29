from lib import *
import json
import json
with open('db.json') as json_file:
    db = json.load(json_file)


def CheckLetters(x, str):
    while not x.isalpha():
        x = input("Please enter correct {}: ".format(str))
    return x


def InfoInput():
    order = input('''If you want to register, press 1,
If you want to login, press 2 
If you want to quit, press 0
What do you want to do ? ''').lower()
    return order

# Input validation
# Checking if the input is empty


def FillGaps(x):
    while not x:
        x = input("Please fill the gaps : ")
    return x
# Validation of Student Code
# REGISTRATION


def CheckUserPassword(x):
    while not x.isdigit() or len(x) != 3:
        x = input("Please enter 3 digits of positive number : ")
    else:
        print("You registered successfully !")
    return x


def CheckUsername(x):
    for i in db['users']:
        while x == i['username']:
            x = input("This username is already taken. Enter new username : ")
    return x

# Duties


def ShowAllData():
    for i in db['users']:
        print(i)


def ShowDataByUsername(x):
    userExists = False
    for i in db['users']:
        if x == i['username']:
            userExists = True
            print(i)
    while userExists == False:
        x = input("There is no such user. Please enter correct username : ")


def CheckUsernameExist(x):
    userExists = False
    for i in db['users']:
        if i['username'] == x:
            userExists = True
    while userExists == False:
        x = input("There is no such user. Please enter correct username : ")
    return x


def CheckRoleExist(x):
    while x != "admin" and x != "editor" and x != "user":
        x = input("There is no such role. Please enter correct role : ").lower()
    return x


def CheckRole(x):
    for i in db['users']:
        if i['username'] == x:
            role = i['role']
    print(f"{x} is an {role}")


def ChangeRole(x, y):
    for i in db['users']:
        if i['username'] == x:
            i['role'] = y.capitalize()
            print(f"You changed the role of {x} to {y.capitalize()}")
# Changing Account


def ChangeAccount(*args):
    db['users'][args[0]]['name'] = args[1]
    db['users'][args[0]]['surname'] = args[2]
    db['users'][args[0]]['username'] = args[3]
    db['users'][args[0]]['password'] = args[4]
    with open("db.json", "w") as json_file:
        json.dump(db, json_file)
# Users


def UserInfo():
    x = input('''If you want to see account info, press "account",
If you want to change account information, press "change",
If you want to quit, press "quit",
What do you want to do? ''')
    return x


def AdminInfo():
    x = input('''If you want to see account info, press "account",
If you want to change account information, press "change",
If you want to see all data, press "all",
If you want to see the info about particular user, press "single",
If you want to change the duties of users, press "duty",
If you want to add new user, press "add",
If you want to quit, press "quit"
What do you want to do? ''')
    return x


def EditorInfo():
    x = input('''If you want to see account info, press "account",
If you want to change account information, press "change",
If you want to see all data, press "all",
If you want to see the info about particular user, press "single",
If you want to quit, press "quit"
What do you want to do? ''')
    return x
