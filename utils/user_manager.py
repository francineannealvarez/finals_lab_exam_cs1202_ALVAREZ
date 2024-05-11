import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()
        self.current_user()


    def load_users(self):
        if not os.path.exists("users.txt"):
            os.makedirs("users.txt") #create file
            open("users.txt", "w").close()
            with open("users.txt") as file: #with to automatically close without the need of close()
                for info in file:
                    username, password = info.strip().split(",")
                    self.users[username] = password

    def save_users(self):
        with open("users.txt", "a") as file:
            for username, password in self.users():
                file.write(f"{username}, {password}\n")
			 
    def validate_username(self, username):
        if len(username) >= 4:
            if username not in self.users:
                return True
            else:
                print("Username already exists.")
        else:
            print("Username must be at least 4 characters long.")

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            print("Password must be at least 8 characters long.")

    def register(self, username, password):
        if self.validate_username and self.validate_password:
            self.users[username] = password
            self.save_users()
            return True
        else:
            return False

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        else:
            return False
