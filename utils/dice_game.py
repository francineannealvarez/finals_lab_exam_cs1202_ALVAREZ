import random
import os
from utils.user import User
from utils.score import Score

class DiceGame(User, Score):
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.scores = {}
        self.current_user = None
        self.load_scores()
        
	
    def load_scores(self):
        try:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split(',')
                    self.scores.append({'username': username, 'game_id': int(game_id), 'points': int(points), 'wins': int(wins)})
        except FileNotFoundError:
            # Create the data folder if it doesn't exist
            os.makedirs('data', exist_ok=True)
        '''
        if not os.path.exists("datafolder.txt"):
            os.makedirs("datafolder.txt") #create file
        if not os.path.exists("datafolder/rankings.txt"):
            f=open("datafolder/rankings.txt", "w")
            f.close()
            self.scores = []
            with open("datafolder/rankings.txt") as file: #with to automatically close without the need of close()
                for line in file:
                    username, game_id, points, wins = line.strip().split(",")
                    score = Score(username, int(game_id))
                    score.points = int(points)
                    score.wins = int(wins)
                    self.scores.append(score)
'''
    def save_scores(self):
        with open("datafolder/rankings.txt", "w") as file:
            for scores in self.scores:
                file.write(f"{scores.username},{scores.game_id},{scores.points},{scores.wins}\n")

    def play_game(self, username):
        stages_won = 0
        self.score = 0
        self.game = True

        while self.game:
            print("New stage begins!")

            for _ in range(3):  # Three rolls per stage
                dice_user = random.randint(1, 6)
                dice_cpu = random.randint(1, 6)
                print(f"{username} rolled: {dice_user}")
                print(f"CPU rolled: {dice_cpu}")

                if dice_user > dice_cpu:
                    print(f"You win this round, {username}!")
                    self.score += 1
                elif dice_user < dice_cpu:
                    print("CPU wins this round!")
                else:
                    print("It's a tie!")

            # Check if the user won the stage
            if self.score % 3 == 0 and self.score > 0:
                stages_won += 1
                print(f"You won stage {stages_won}, {username}!")
            
            print(f"Total Points: {self.score}, Stages won: {stages_won}")

            user_choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
            if user_choice == "0":
                print(f"Game over. You won {stages_won} stages with a total of {self.score} points.")
                break
            elif user_choice != "1":
                print("Invalid input. Please enter 1 for Yes and 0 for No.")




    def show_top_scores():
        pass
    
    def logout(self):
        self.current_user = None
        
    def menu(self):
        while True:
            print("Main Menu")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                if not username.strip():  # Check if input is blank
                    print("Register failed.")
                    return
                password = input("Enter password: ")
                if not password.strip():  # Check if input is blank
                    print("Register failed.")
                    return
                if self.user_manager.register(username, password):
                    print("Registered successfully.")
                else:
                    print("Registration failed. Please try again.")
            elif choice == "2":
                username = input("Enter username: ")
                if not username.strip():  # Check if input is blank
                    print("Login failed.")
                    return
                password = input("Enter password, or leave blank to cancel:")
                if not password.strip():  # Check if input is blank
                    print("Login failed.")
                    return
                if self.user_manager.login(username, password):
                    print("Logged in successfully.")
                    self.current_user = User(username, password)
                    self.user_menu(username)
                else:
                    print("Invalid username or password.")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
            
    def user_menu(self, username):
        print(f"Welcome {username}!")
        print("Menu: ")
        print("1. Start Game")
        print("2. Show Top Scores ")
        print("3. Log out")
        user_choice = input("Enter your choice, or leave blank to cancel: ")
        if not user_choice.strip():  # Check if input is blank
            return
        
        if user_choice == "1":
            self.play_game(username)
        elif user_choice == "2":
            self.show_top_scores() 
        elif user_choice == "3":
            self.logout()
            print(f"Goodbye {username}")
            print("You Logged out successfully.")
        else:
            print("Invalid choice.")
'''
    def register(self):
        print("\nRegister User Page")
        username = input("Enter username (at least 4 characters) or leave blank to cancel: ")
        if not username.strip():  # Check if input is blank
            print("Register failed.")
            return
        password = input("Enter password (at least 8 characters) or leave blank to cancel: ")
        if not password.strip():  # Check if input is blank
            print("Register failed.")
            return
        if self.user_manager.register(username, password):
            print("Registered successfully.")
        else:
            print("Registration failed. Please try again.")

    def login(self, username, password):
        print("\nLogin")
        username = input("Enter username, or leave blank to cancel:")
        if not username.strip():  # Check if input is blank
            print("Login failed.")
            return
        password = input("Enter password, or leave blank to cancel:")
        if not password.strip():  # Check if input is blank
            print("Login failed.")
            return
        if self.user_manager.login(username, password):
            print("Logged in successfully.")
            self.current_user = User(username, password)
            self.user_menu()
        else:
            print("Invalid username or password.")'''
    