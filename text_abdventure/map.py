import random
from monster import *

class TutorialMap():
	def __init__(self):
		self.player_board = []
		self.board = []
		self.x = 0
		self.y = 0
		for i in range(5):
			field = []
			for j in range(5):
				field.append("-")
			self.board.append(field)
		self.board[self.x][self.y] = "P"
		self.board[self.x][1] = "O"

		for i in range(5):
			field = []
			for j in range(5):
				field.append("-")
			self.player_board.append(field)
		self.player_board[0][0] = "P"

	def print_map(self):
		for i in self.player_board:
			print(i)
		

class LevelOneMap():
	def __init__(self):

		self.monster = ["O", "L", "K"]
		self.interactions = ["C", "D", "F", "|"]
		self.elements = ["O", "L", "K", "C", "D", "F", "|", "", "", "", ""]
		self.elements_check = ["O", "L", "K", "C", "D", "F", "|"]
		self.monster_counter = 10
		self.chest = 4
		self.door = 1 
		self.falldoor = 3
		self.wall = 10
		self.check = [self.monster_counter, self.chest, self.door, self.falldoor, self.wall]

		self.board = []
		self.player_board = []
		self.x = 0
		self.y = 0

		self.next_level = False
		self.item = ""
		self.items = ["HP-", "AP-", "S1-", "A1-"]

		for i in range(10):
			field = []
			for j in range(5):
				field.append("-")
			self.player_board.append(field)
		self.player_board[0][0] = "P"

		for i in range(10):
			field = []
			for j in range(5):
				field.append("-")
			self.board.append(field)

		self.create_map()
		self.board[0][0] = "P"

	# create hidden map	
	def create_map(self):
		self.skip = False
		self.element = ""
		for li in range(10):
			if self.skip == True:
				break
			for i in range(5):
				for j in self.check:
					if j > 0:
						break
					else:
						self.skip = True
				if self.skip == True:
					break

				self.element = self.elements[random.randint(0, 10)]

				if self.element in self.monster and self.monster_counter > 0:
					self.monster_counter -= 1
					self.board[li][i] = self.element

				elif self.element in self.interactions:
					if self.element == "C" and self.chest > 0:
						self.chest -= 1
						self.board[li][i] = self.element
					elif self.element == "D" and self.door > 0:
						self.door -= 1
						self.board[li][i] = self.element
					elif self.element == "F" and self.falldoor > 0:
						self.falldoor -= 1
						self.board[li][i] = self.element
					elif self.element == "|" and self.wall > 0:
						self.wall -= 1
						self.board[li][i] = self.element

	# print map
	def print_map(self):
		for i in self.player_board:
			print(i)
		print("")

	# react to field	
	def check_field_no_element(self):
		if self.board[self.x][self.y] not in self.elements_check:
				self.board[self.x][self.y] = " "
				self.player_board[self.x][self.y] = " "

	# check if there is a wall
	def check_if_wall(self):
		if self.board[self.x][self.y] == "|":
			print("There is a wall, you can´t move")
			return True
		return False

	# react to field
	def check_field(self, player):
		if self.board[self.x][self.y] == "-" or self.board[self.x][self.y] == " ":
			self.board[self.x][self.y] = "P"
			self.player_board[self.x][self.y] = "P"

		elif self.board[self.x][self.y] == "C":
			print("oh there is a chest, you get some item")
			self.item = self.items[random.randint(0, 3)]
			print("This is the item you get: ", self.item, "\n")
			self.board[self.x][self.y] = "P"
			self.player_board[self.x][self.y] = "P"

		elif self.board[self.x][self.y] == "D":
			while True:
				self.next_level = input("You wanna go to the next Level [True/False]:\n~ ").lower()
				if self.next_level == "true":
					self.next_level = True
					break
				elif self.next_level == "false":
					self.player_board[self.x][self.y] = "D"
					break

		elif self.board[self.x][self.y] == "F":
			print("You fall down and die, Try again :/")
			quit()

		elif self.board[self.x][self.y] in self.monster:
			self.monster_obj = Monster(self.board[self.x][self.y], 1, player)

	# movement		
	def left(self, player):
		if self.y > 0:
			self.check_field_no_element()
			self.y -= 1
			is_wall = self.check_if_wall()
			if is_wall == False:
				self.check_field(player)
			else:
				self.player_board[self.x][self.y] = "|"
				self.y += 1
				self.player_board[self.x][self.y] = "P"
				self.board[self.x][self.y] = "P"
		else:
			print("Move unavaible")

	def right(self, player):
		if self.y < len(self.board[0])-1:
			self.check_field_no_element()
			self.y += 1
			is_wall = self.check_if_wall()
			if is_wall == False:
				self.check_field(player)
			else:
				self.player_board[self.x][self.y] = "|"
				self.y -= 1
				self.player_board[self.x][self.y] = "P"
				self.board[self.x][self.y] = "P"
		else:
			print("Move unavaible")

	def forward(self, player):
		if self.x > 0:
			self.check_field_no_element()
			self.x -= 1
			is_wall = self.check_if_wall()
			if is_wall == False:
				self.check_field(player)
			else:
				self.player_board[self.x][self.y] = "|"
				self.x += 1	
				self.player_board[self.x][self.y] = "P"
				self.board[self.x][self.y] = "P"	
		else:
			print("Move unavaible")

	def backward(self, player):
		if self.x < len(self.board)-1:
			self.check_field_no_element()
			self.x += 1
			is_wall = self.check_if_wall()
			if is_wall == False:
				self.check_field(player)
			else:
				self.player_board[self.x][self.y] = "|"
				self.x -= 1		
				self.player_board[self.x][self.y] = "P"
				self.board[self.x][self.y] = "P"
		else:
			print("Move unavaible")