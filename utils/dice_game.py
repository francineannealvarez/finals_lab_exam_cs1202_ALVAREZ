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
	
    
		