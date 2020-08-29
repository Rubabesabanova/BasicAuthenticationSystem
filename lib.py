import json
with open('db.json') as json_file:
    db = json.load(json_file)


class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password
        self.role = "User"
        self.addDataToDict()

    def addDataToDict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    def addToJson(self):
        db['users'].append(self.addDataToDict())
        with open("db.json", "w") as json_file:
            json.dump(db, json_file)


class AdminUser(User):
    def __init__(self, _name, _surname, _username, _password):
        super(AdminUser, self).__init__(_name, _surname, _username, _password)
        self.role = "Admin"


class EditorUser(User):
    def __init__(self, _name, _surname, _username, _password):
        super(EditorUser, self).__init__(_name, _surname, _username, _password)
        self.role = "Editor"


