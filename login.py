from functions import *
import json
with open('db.json') as json_file:
    db = json.load(json_file)
def login():
    l_username = input("Username : ")
    l_username = FillGaps(l_username)
    l_username = loginusername(l_username)
    while l_username == 7:
        l_username = loginusername(input("False username : "))
    password = input("Password : ")
    password = FillGaps(password)
    while db[l_username]["password"] != password:
        password = input("False password : ")
    print("You logged in as {} successfully ! ".format(db[l_username]["role"]))
    return l_username

def loginusername(x):
    for i in range(len(db)):
        if db[i]['username'] == x:
            return i
    return 7

