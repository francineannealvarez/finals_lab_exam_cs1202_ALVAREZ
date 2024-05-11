class DiceGame:
	
    def load_scores():
        pass

    def save_scores():
        pass

    def play_game():
        pass

    def show_top_scores():
        pass
    
    def logout():
        pass
        
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
            print("Logged out successfully.")
        else:
            print("Invalid choice.")


		