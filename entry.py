from functions import *
from register import *
from login import *
import json
with open('db.json') as json_file:
    db = json.load(json_file)

def ExecuteOrders():
    order = InfoInput()
    while order != "0":
        if order == "1":
            registerorder = input(
                "Do you want to register as Admin, Editor or User ? ").lower()
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
                    registerorder = input(
                        "Please type correct keyword : ").lower()
            order = InfoInput()
        elif order == "2":
            l_username = login()
            if db[l_username]['role'] == 'Admin':
                admininfo = AdminInfo().lower()
                while True:
                    if admininfo == "all":
                        ShowAllData()
                        admininfo = AdminInfo().lower()
                    elif admininfo == "account":
                        print(db[l_username])
                        admininfo = AdminInfo().lower()
                    elif admininfo == "single":
                        showUser = input(
                            'Enter the username you want to know about : ')
                        showUser = CheckUsernameExist(showUser)
                        ShowDataByUsername(showUser)
                        admininfo = AdminInfo().lower()
                    elif admininfo == "duty":
                        changeUser = input(
                            'Enter the username you want to change : ')
                        changeUser = CheckUsernameExist(changeUser)
                        CheckRole(changeUser)
                        changeRole = input('''1. User,
2. Editor,
3. Admin
To which position you want to change the user(type user, editor or admin) : ''').lower()
                        changeRole = CheckRoleExist(changeRole)
                        ChangeRole(changeUser, changeRole)
                        admininfo = AdminInfo().lower()
                    elif admininfo == "quit":
                        break
                    else:
                        admininfo = input("Please type correct keyword : ")
                order = InfoInput()
            elif db[l_username]['role'] == 'Editor':
                editorinfo = EditorInfo().lower()
                while True:
                    if editorinfo == "all":
                        ShowAllData()
                        editorinfo = EditorInfo().lower()
                    elif editorinfo == "account":
                        print(db[l_username])
                        editorinfo = EditorInfo().lower()
                    elif editorinfo == "single":
                        showUser = input(
                            'Enter the username you want to know about : ')
                        showUser = CheckUsernameExist(showUser)
                        ShowDataByUsername(showUser)
                        editorinfo = EditorInfo().lower()
                    elif editorinfo == "quit":
                        break
                    else:
                        editorinfo = input("Please type correct keyword : ")
                order = InfoInput()
            elif db[l_username]['role'] == 'User':
                userinfo = UserInfo().lower()
                while True:
                    if userinfo == "all":
                        ShowAllData()
                        userinfo = UserInfo().lower()
                    elif userinfo == "account":
                        print(db[l_username])
                        userinfo = UserInfo().lower()
                    elif userinfo == "quit":
                        break
                    else:
                        userinfo = input("Please type correct keyword : ")
                order = InfoInput()
        else:
            order = input("Please type correct keyword : ").lower()
    else:
        print("Good luck !")


ExecuteOrders()

print(data)
