

class Main():
	def main():
		user_manager = UserManager()
		dice_game = DiceGame(user_manager)
		dice_game.menu()

	if __name__ == "__main__":
		main()