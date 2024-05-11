import os
from utils.user import User
from utils.dice_game import *

diceGame = DiceGame()

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = password
        except FileNotFoundError:
            print("No existing user data found.")
        except Exception as e:
            print(f"Error occurred while loading users: {e}")

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

    def register(self):
        while True:
            username = input("Enter username: ")
            if not username.strip():
                print("Canceled.")
                return
            password = input("Enter password: ")
            if not password.strip():
                print("Canceled.")
                return
            if self.validate_username(username) and self.validate_password(password):
                if username in self.users:
                    print("Username already exists.")
                else: 
                    self.users[username] = User(username, password)
                    self.save_users()
                    print("Registration successful.")
                    return True
            else:
                print("Registration failed. Please try again.")
                return False

    def login(self):
        username = input("Enter username: ")
        if not username.strip():
            print("Login failed.")
            return

        if username in self.users:
            password = input("Enter password, or leave blank to cancel: ")
            if not password.strip():
                print("Login canceled.")
                return

            if self.users[username].password == password:
                print("Logged in successfully.")
                self.current_user = username
                diceGame.game_menu(username)
            else:
                print("Invalid username or password.")
        else:
            print("Username does not exist.")
