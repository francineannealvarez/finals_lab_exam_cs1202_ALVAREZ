import random
import os
from datetime import datetime
from utils.score import *
from utils.user import *


class DiceGame:
    def __init__(self):
        self.scores = {}
        self.users = {}
        self.current_user = None
        self.load_scores()

        
        '''
    def load_scores(self):
        try:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split(',')
                    self.scores.append({'username': username, 'game_id': int(game_id), 'points': int(points), 'wins': int(wins)})
        except FileNotFoundError:
            # Create the data folder if it doesn't exist
            os.makedirs('data', exist_ok=True)
            
        
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

    def save_scores(self):
        with open("datafolder/rankings.txt", "w") as file:
            for scores in self.scores:
                file.write(f"{scores.username},{scores.game_id},{scores.points},{scores.wins}\n")
'''

    def play_game(self, username):
        while True:
            stages_won = 0
            self.score = 0

            for stage in range(3):  # Three stages of the game
                wins = 0
                print(f"Stage {stage + 1} begins!")

                for roll in range(3):  # Three rolls per stage
                    dice_user = random.randint(1, 6)
                    dice_cpu = random.randint(1, 6)
                    print(f"{username} rolled: {dice_user}")
                    print(f"CPU rolled: {dice_cpu}")

                    if dice_user > dice_cpu:
                        print(f"You win this round, {username}!")
                        self.score += 1
                        wins += 1
                    elif dice_user < dice_cpu:
                        print("CPU wins this round!")
                    else:
                        print("It's a tie!")

                if wins >= 2:
                    self.score += 3
                    stages_won += 1
                    print(f"You won this stage, {username}!")
                    user_choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                    if user_choice == "0":
                        print(f"Game over. You won {stages_won} stages with a total of {self.score} points.")
                        self.save_score(username, self.score, stages_won)
                        self.game_menu(username)
                        return
                    elif user_choice == "1":
                        continue
                    else:
                        print("Invalid input. Please enter 1 for Yes and 0 for No.")
                else: 
                    print(f"You lost this stage, {username}")
                    print("Game over. You didn't win any stages.")
                    self.game_menu(username)
                    return
                    
                    
                print(f"Total Points: {self.score}, Stages won: {stages_won}")
                self.game_menu(username)

    def load_scores(self):
        try:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        username, game_id, points, wins = data
                        self.scores[len(self.scores)] = {'username': username, 'game_id': int(game_id), 'points': int(points), 'wins': int(wins)}
                    else:
                        print(f"Ignore line: {line.strip()} - Insufficient data")
        except FileNotFoundError:
            os.makedirs('data', exist_ok=True)



    def save_score(self, username, points, wins):
        game_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        try:
            with open("data/rankings.txt", "a") as file:
                file.write(f"{username},{game_id},{points},{wins}\n")
        except FileNotFoundError:
            print("Error: Could not save score. File not found.")

    def show_top_scores(self, username):
        try:
            with open("data/rankings.txt", "r") as file:
                scores = [line.strip().split(",") for line in file.readlines()]
                scores.sort(key=lambda x: int(x[2]), reverse=True)  # Sort by points
                print("Top 10 Scores:")
                for i, score in enumerate(scores[:10], start=1):
                    if len(score) >= 4:
                        print(f"{i}. Username: {score[0]}: Points - {score[2]}, Wins - {score[3]}")
                    else:
                        print("No games played yet. Play a game to see top scores.")
            self.game_menu(username)
        except FileNotFoundError:
            print("No scores recorded yet.")



    def logout(self):
        return
        
    def game_menu(self, username):
        print(f"Welcome {username}!")
        print("Menu: ")
        print("1. Start Game")
        print("2. Show Top Scores ")
        print("3. Log out")
        user_choice = input("Enter your choice, or leave blank to cancel: ")
        if not user_choice.strip():  # Check if input is blank
            return
        else: 
            if user_choice == "1":
                self.play_game(username)
            elif user_choice == "2":
                self.show_top_scores(username) 
            elif user_choice == "3":
                print(f"Goodbye {username}")
                print("You Logged out successfully.")
                self.logout()
            else:
                print("Invalid choice.")