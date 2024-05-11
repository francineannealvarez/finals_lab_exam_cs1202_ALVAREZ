import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("users.txt", "w") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = password
        except Exception as e:
            print(f"Error occured: {e}")
            # Create the data directory if it doesn't exist
           # if not os.path.exists("data"):
                #os.makedirs("data")

            # Create the users.txt file if it doesn't exist
            #if not os.path.exists("data/users.txt"):
               # open("data/users.txt", "w").close()  

            # Read user information from the file
            


    def save_users(self):
        try:
            with open("users.txt", "w") as file:
                for username, password in self.users.items():
                    file.write(f"{username},{password}\n")
        except Exception as e:
            print(f"Error occurred while saving users: {e}")
			 
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
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
