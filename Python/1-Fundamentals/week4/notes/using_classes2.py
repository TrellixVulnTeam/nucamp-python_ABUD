class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("eric", "eric@nucamp.co", "ericsCoolPassword")
print(user1.password)


user1.change_password("betterPassword")
