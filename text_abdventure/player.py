class Player:
	def __init__(self, level):
		if level == 1:
			self.hp = 100
			self.hp_limit = 100
			self.attack = 20
			self.armor = 0