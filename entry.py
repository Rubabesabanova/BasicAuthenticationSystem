from functions import *
from register import *
from login import *
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

ExecuteOrders()
for i in range(len(db)):
    db[i].ShowData()


