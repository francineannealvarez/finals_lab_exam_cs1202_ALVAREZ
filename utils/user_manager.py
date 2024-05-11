import os

class UserManager:
	def __init__(self, users):
		self.users = {}
		self.load_users()

	def load_users(self):
		if not os.path.exists("users.txt"):
			os.makedirs("users.txt") #create file
			f=open("users.txt", "w")
			f.close()
			with open("users.txt") as file:
				for info in file:
					username, password = info.strip().split(",")
					self.users[username] = password
	
			
		
     


	def save_users():
		pass

	def validate_username():
		pass

	def validate_password():
		pass

	def register():
		pass

	def login():
		pass
