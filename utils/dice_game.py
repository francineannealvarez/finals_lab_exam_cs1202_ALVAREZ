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
        current_user = user_manager.current_user
        if current_user:
            User.__init__(self, current_user.username, current_user.password)
            Score.__init__(self, current_user.username)  # Assuming game_id is defined
        else:
            User.__init__(self, "", "")  # Initialize with empty username and password
            Score.__init__(self, "", "")  # Initialize with empty username and game_id



	
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
        stages = 3
        stages_won = 0
        while True:
            dice_user = random.randint(1,6) 
            dice_cpu = random.randint(1,6) 
            print(f"{username} rolled: {dice_user}")    
            print(f"CPU rolled: {dice_cpu}")
            if dice_user > dice_cpu:
                    print(f"You win this round {username}!")
                    stages -= 1
                    self.score += 1
                    self.wins +=1
                    if stages == 0:
                        self.game = False
                    else:
                        continue
            elif dice_user < dice_cpu:
                    print(f"CPU wins this round!")
                    stages -= 1
                    if stages == 0:
                        self.game = False
                    else:
                        continue
            elif dice_user == dice_cpu:
                    print(f"It's a tie!")
                    stages -= 1
                    if stages == 0:
                        self.game = False
                    else:
                        continue
            if self.wins >= 2:
                self.score += 3
                stages_won += 1
                print(f"You won this stage {username}")
                print(f"Total Points: {self.score},Stages won: {stages_won}")
                user_choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No)")
                if user_choice == "1":
                    continue
                elif user_choice == "0":
                    print(f"Game over. You won {stages_won} with a total of {self.score} points.")
                else: 
                    print("Invalid input. Please enter 1 for Yes and 0 for No.")


    def show_top_scores():
        pass
    
    def logout(self):
        self.current_user = None
        
    def menu():
        pass

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
            print("Invalid username or password.")

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
            self.play_game()
        elif user_choice == "2":
            self.show_top_scores() 
        elif user_choice == "3":
            self.logout()
            print(f"Goodbye {username}")
            print("You Logged out successfully.")
        else:
            print("Invalid choice.")


		