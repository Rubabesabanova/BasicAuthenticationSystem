from functions import *

def Registration():
    name = input("Name : ").lower()
    name = FillGaps(name)
    name = CheckLetters(name, "name")
    surname = input("Surname : ").lower()
    surname = FillGaps(surname)
    surname = CheckLetters(surname, "surname")
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
