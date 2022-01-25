import time
from map import Tutorial_Map

m = Tutorial_Map()

def print_Commands():
	for index, cmd in enumerate(Commands):
		print(index, "->", cmd)

def print_map():
	pass

def print_position():
	pass

def left():
	pass

def right():
	pass

def forward():
	pass

def backward():
	pass

def fight():
	pass

def print_hp():
	pass

def print_character_values():
	pass

def print_inventar():
	pass

def get_item_info():
	pass

def use_item():
	pass

Commands = {
    "help": print_Commands,
	"print_map": print_map,
	"print_position": print_position,
    "left": left,
    "right": right,
    "forward": forward,
    "backward": backward,
    "fight": fight,
    "print_hp": print_hp,
    "print_character_values": print_character_values,
    "print_inventar": print_inventar,
    "get_item_info": get_item_info,
    "use_item": use_item
}

class Tutorial():
	def __init__(self):

		while True:
			skip = input("Do you wanna skip the tutorial[true/false]:\n~ ")
			if skip == "true" or skip == "false":
				break
		if skip == "false":
			self.welcome()
			print("You have some commands:")
			print_Commands()
			print("Typ -> help to get a list of all commands\nhere you can see the map:\n")
			time.sleep(3)
			Commands["print_map"]()
			print("")
			while True:
				go_on = input("Can we go on [Y]:\n~ ").lower()
				if go_on == "y":
					break

			print("You can move with the commands:\n<- left\n\nright ->\n\n^ forward\n|\n\n| backward\nv\n")
			time.sleep(5)
			print("But with your current position you can´t go left:\n")
			print("Move unavaible")
			print("-> This is the result when you try to move out of the map")
			time.sleep(2)
			print("\nYou have 100 hp\nYour attack is 20\nYou can collect Armor, which increase your Damage resistens")
			print("When your hp are 0, you die!")
			time.sleep(1)
			print("There are also some enemys like the Orks")
			print("You can also collect some heal potion and other items")
			print("You can collect items by get on a field with a chest (C)")
			time.sleep(1)
			print("But there can also be walls or a falldoor (you fall down and die)")
			time.sleep(1)
			print("With the comand -> print_inventar, you can see all your items")
			print("Last but not least, you need to know, that you reach the next level by open the door [quit game by type quit]")
			print("Ok, now you should be ready to go alone at the battelfield\n\n\n")
		

	def welcome(self):
		print("Welcome to jungle...")
		time.sleep(1)
		print("I mean not to the jungle...")
		time.sleep(1)
		print("You need to find your daughter")
		time.sleep(1)
		print("You began at the lowest floor of the castle")
		time.sleep(1)
		print("Now at the lowest floor you get some help, but after this floor you have to fight alone!!")
