class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password
        self.role="User"

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
