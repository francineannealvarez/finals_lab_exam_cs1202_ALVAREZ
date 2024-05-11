from utils.user_manager import UserManager
from utils.dice_game import DiceGame
from utils.user import User

user_manager=UserManager()

def main():
    user_manager.load_users()
    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        user_choice = input("Enter the number corresponding to your choice: ")
        
        if user_choice == "1":
            user_manager.register()
        elif user_choice == "2":
            user_manager.login()
        elif user_choice == "3":
            print("Exiting")
            break

if __name__ == "__main__":
    main()
