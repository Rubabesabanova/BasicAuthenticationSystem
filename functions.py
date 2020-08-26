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
What do you want to do ? ''').lower()
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
# Checking if the input is empty

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
        while x == i.username:
            x = input("This username is already taken. Enter new username : ")
    return x

