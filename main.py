from utils.user_manager import UserManager
from utils.dice_game import DiceGame
'''
class Main(UserManager, DiceGame):
	def __init__(self):
		UserManager.__init__(self)
		DiceGame.__init__(self)
'''
'''
def main():
    user_manager = UserManager(User)
    dice_game = DiceGame(user_manager)
    while True:
        print("Welcome to the Dice Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            UserManager.register()
        elif choice == "2":
            UserManager.login()
            if DiceGame.current_user:
                DiceGame.user_menu()
        elif choice == "3":
            print("Exiting Game")
            break
        else:
            print("Invalid choice")
'''

def main():
    user_manager = UserManager()
    dice_game = DiceGame(user_manager)
    dice_game.menu()
    
if __name__ == "__main__":
    main()
