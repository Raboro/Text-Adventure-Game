from player import * # Player
from initiation import * # Initiation
from tutorial import * #  Tutorial
from level_1 import * # Level 1


# Start
if __name__ == '__main__':
	while True:
			player_name = input("Please select you name:\n~ ")
			if player_name == "":
				print("Try again")
			else: 
				break

	print(f"Welcome {player_name}")

	player_obj = Player(0)

	initiation_obj = Initiation()
	tutorial_obj = Tutorial()
	level_1_obj = LevelOne()