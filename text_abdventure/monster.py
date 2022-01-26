import time

class Monster:
	def __init__(self, monster, level, player):
		self.monster = monster
		if level == 1:
			self.monster_level_one(self.monster, player)
		elif level == 2:
			self.monster_level_two(self.monster, player)
		else:
			pass

	# info about player and monster
	def get_character_info(self, player):
		print(f"\nPlayer: \nAttack -> {player.attack} \nHeath -> {player.hp} \nArmor -> {player.armor}\n")
		if self.monster_hp > 0:
			print(f"{self.name}: \nAttack -> {self.monster_at} \nHealth -> {self.monster_hp}\n")


	# player fight with monster
	def fight(self, monster_at, monster_hp, name, player):
		self.counter = 1
		self.monster_at = monster_at
		self.monster_hp = monster_hp
		self.name = name

		while True:
			time.sleep(2)
			self.get_character_info(player)
			print(f"\nRunde:  {self.counter}, fight\n")
			time.sleep(2)
			self.monster_hp -= player.attack
			player.hp -= (self.monster_at - player.armor)
			self.counter += 1

			if self.monster_hp <= 0 and player.hp > 0:
				print("You won")
				break

			elif player.hp <= 0:
				print("You are dead, try again :/")
				quit()
				break
			
	# get/select the right monster
	def monster_level_one(self, monster, player):
		if self.monster == "O":
			print("Oh shit, a Ork")
			self.fight(20, 20, "Ork", player)
			return True

		elif self.monster == "L":
			print("Oh shit, a Lellek")
			self.fight(50, 40, "Lellek", player)
			return True

		elif self.monster == "K":
			print("Oh shit, a Kobold")
			self.fight(40, 60, "Kobold", player)
			return True

		return False


	def monster_level_two(self, monster):
		self.info = self.monster_level_one(self.monster)
		if self.info == False:
			pass
		else:
			pass	
