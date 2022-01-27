from player import * # Player
from initiation import * # Initiation
from tutorial import * #  Tutorial
from level_1 import * # Level 1

import pickle


# Start
if __name__ == '__main__':
	while True:
			player_name = input("Please select you name:\n~ ")
			if player_name == "":
				print("Try again")
			else: 
				break

	print(f"Welcome {player_name}")

	#level = 1
	#with open("save_level.pickle", "wb") as pickle_file:
		#pickle.dump(player_name, pickle_file)

	#with open("save_level.pickle", "rb") as pickle_file:
	#	save_level = pickle.load(pickle_file)

	#print(save_level)

	initiation_obj = Initiation()
	tutorial_obj = Tutorial()
	level_1_obj = LevelOne()