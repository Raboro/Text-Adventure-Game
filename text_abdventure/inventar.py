class Inventar():
	def __init__(self):
		self.inventar_list = []
		for i in range(30):
			self.inventar_list.append("---") 

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
	
	def use_item(self, items):
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
				if self.selected_item != "---" and self.selected_item != 100:
					print("ok")
					break
				else:
					print("Wrong, please select a item")