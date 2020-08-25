from lib import *
from db import db


def CheckLetters(x, str):
    while not x.isalpha():
        x = input("Please enter correct {}: ".format(str))
    return x


def InfoInput():
    order = input('''If you want to register, press 1,
If you want to login, press 2 
If you want to quit, press 0
Do you want to register or login ? ''').lower()
    return order


def ExecuteOrders():
    order = InfoInput()
    while order != "0":
        if order == "1":
            registerorder = input("Do you want to register as Admin, Editor or User ? ").lower()
            while True:
                if registerorder == "admin":
                    PlacingAdminstoDb()
                    break
                elif registerorder == "editor":
                    PlacingEditorstoDb()
                    break
                elif registerorder == "user":
                    PlacingUserstoDb()
                    break
                else:
                    registerorder = input("Please type correct keyword : ").lower()
            order = InfoInput()
        elif order == "2":
            login()
            order = InfoInput()
        else:
            order = input("Please type correct keyword : ").lower()
    else:
        print("Good luck !")


# Input validation
# Cheking if the input is empty


def FillGaps(x):
    while not x:
        x = input("Please fill the gaps : ")
    return x


# Validation of Student Code
# REGISTRATION
def CheckUserPassword(x):
    while not x.isdigit() or len(x) != 6:
        x = input("Please enter 6 digits of positive number : ")
    else:
        print("You registered successfully !")
    return x


def CheckUsername(x):
    for i in db:
        if x == i.username:
            x = input("This username is already taken. Enter new username : ")
    return x


def Registration():
    name = input("Name : ").lower()
    name = FillGaps(name)
    name = CheckLetters(name, "name")
    surname = input("Surname : ").lower()
    surname = FillGaps(surname)
    surname = CheckLetters(name, "surname")
    username = input("Username : ")
    username = FillGaps(username)
    username = CheckUsername(username)
    password = input("Password : ")
    password = FillGaps(password)
    password = CheckUserPassword(password)
    return [name, surname, username, password]


def PlacingUserstoDb():
    user = User(*Registration())
    db.append(user)


def PlacingAdminstoDb():
    admin = AdminUser(*Registration())
    db.append(admin)


def PlacingEditorstoDb():
    editor = EditorUser(*Registration())
    db.append(editor)


# LOGIN
def login():
    l_username = input("Username : ")
    l_username = FillGaps(l_username)
    l_username = loginusername(l_username)
    while l_username == -1:
        l_username = loginusername(input("False username : "))
    password = input("Password : ")
    password = FillGaps(password)
    while db[l_username].password != password:
        password = input("False password : ")
    print("You logged in as {} successfully ! ".format(db[l_username].role))


def loginusername(x):
    for i in range(len(db)):
        if db[i].username == x:
            return i
    return -1
