import os

class UserManager:
	def __init__(self, users):
		self.users = {} #empty dictionary
		self.load_users() #invoke load_users function

	def load_users(self):
		if not os.path.exists("users.txt"):
			os.makedirs("users.txt") #create file
			f=open("users.txt", "w")
			f.close()
			with open("users.txt") as file: #with to automatically close without the need of close()
				for info in file:
					username, password = info.strip().split(",")
					self.users[username] = password

	def save_users():
		with open("users.txt", "a") as file:
			for username, password in self.users():
				file.write(f"{username}, {password}\n")
			 
	def validate_username(self, username):
		if len(username) >= 4 and username not in self.users:
			return True
		else:
			return False

	def validate_password():
		if len(password) >= 8:
			return True
		else:
			return False

	def register():
		pass

	def login():
		pass
