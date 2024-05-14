from utils.user_manager import *

user_manager = UserManager()

def main():
    user_manager.load_users()
    while True:
        
        print("\nWelcome to Dice Roll Game!")
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
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
