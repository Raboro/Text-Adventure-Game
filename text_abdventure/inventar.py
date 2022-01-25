class Inventar():
	def __init__(self):
		self.sword_counter = 0
		self.armor_counter = 0

		self.inventar_list = []
		for i in range(30):
			self.inventar_list.append("---") 

		self.reload()

	def reload(self):
		self.inventar_print = [
			["-------------------------------------------------------------------------"],
			["|", self.inventar_list[0], "|", self.inventar_list[1], "|", self.inventar_list[2], "|", self.inventar_list[3], "|", self.inventar_list[4], "|", self.inventar_list[5], "|"],
			["|", "001", "|", "002", "|", "003", "|", "004", "|", "005", "|", "006", "|"],
			["-------------------------------------------------------------------------"],
			["|", self.inventar_list[6], "|", self.inventar_list[7], "|", self.inventar_list[8], "|", self.inventar_list[9], "|", self.inventar_list[10], "|", self.inventar_list[11], "|"],
			["|", "007", "|", "008", "|", "009", "|", "010", "|", "011", "|", "012", "|"],
			["-------------------------------------------------------------------------"],
			["|", self.inventar_list[12], "|", self.inventar_list[13], "|", self.inventar_list[14], "|", self.inventar_list[15], "|", self.inventar_list[16], "|", self.inventar_list[17], "|"],
			["|", "013", "|", "014", "|", "015", "|", "016", "|", "017", "|", "018", "|"],
			["-------------------------------------------------------------------------"],
			["|", self.inventar_list[18], "|", self.inventar_list[19], "|", self.inventar_list[20], "|", self.inventar_list[21], "|", self.inventar_list[22], "|", self.inventar_list[23], "|"],
			["|", "019", "|", "020", "|", "021", "|", "022", "|", "023", "|", "024", "|"],
			["-------------------------------------------------------------------------"],
			["|", self.inventar_list[24], "|", self.inventar_list[25], "|", self.inventar_list[26], "|", self.inventar_list[27], "|", self.inventar_list[28], "|", self.inventar_list[29], "|"],
			["|", "025", "|", "026", "|", "027", "|", "028", "|", "029", "|", "030", "|"],
			["-------------------------------------------------------------------------"]
		]
	
	def use_selected_item(self, player):
		if self.selected_item == "HP-":
			if player.hp + 50 <= player.hp_limit:
				player.hp += 50

			else:
				player.hp = player.hp_limit

		elif self.selected_item == "AP-":
			player.attack += 50

		elif self.selected_item == "S1-":
			if self.sword_counter == 0:
				self.sword_counter += 1
				player.attack += 20

			else:
				print("You already have a sword equiped")

		elif self.selected_item == "A1-":
			if self.armor_counter <= 7:
				self.armor_counter += 1
				player.armor += 5
				player.hp_limit += 30

			else:
				print("You cant equip more armor")	


	def remove_item(self):
		for i in range(len(self.inventar_list)):
			if self.inventar_list[i] == self.selected_item:
				self.inventar_list[i] = "---"
				self.reload()
				break


	def use_item(self, items, player):
		for i in self.inventar_print:
			print(i)

		while True:
			self.quit = input("Are you sure you will use a item [Yes/No]:\n~ ").lower()
			if self.quit == "yes" or self.quit == "no":
				break
			else:
				print("Please type the right words!")
		if self.quit == "yes":
			while True:
				self.selected_item = self.inventar_list[int(input("Select a item, by type his number:\n~ "))-1]
				if self.selected_item != "---":
					self.use_selected_item(player)
					self.remove_item()
					break
				else:
					print("Wrong, please select a item")