import json
data=[]

class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password
        self.role="User"
        self.addDataToDict()

    def addDataToDict(self):
        myDict = dict()
        myDict['name']= self.name
        myDict['surname']= self.surname
        myDict['username']= self.username
        myDict['password']= self.password
        myDict['role']= self.role
        data.append(myDict)
        with open("db.json", "w") as conn:
            json.dump(data, conn)
    def ShowData(self):
        print(f"Name : {self.name}, Surname : {self.surname}, Username : {self.username}, Role : {self.role}")


class AdminUser(User):
    def __init__(self, _name, _surname, _username, _password):
        super(AdminUser, self).__init__( _name, _surname, _username, _password)
        self.role="Admin"

class EditorUser(User):
    def __init__(self, _name, _surname, _username, _password):
        super(EditorUser, self).__init__( _name, _surname, _username, _password)
        self.role="Editor"


