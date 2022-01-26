from map import LevelOneMap
from player import *
from inventar import *
import time

# generate objects
m = LevelOneMap()
player = Player(1)
inventar = Inventar()

# print all Commands
def print_Commands():
	for index, cmd in enumerate(Commands):
		if index < 10:
			print(f"{index}  -> {cmd}")
		else:
			print(f"{index} -> {cmd}")

# print the map
def print_map():
	m.print_map()

# print position on the map
def print_position():
	print(f"{m.x}, {m.y}")

# move left
def left():
	m.left(player)

# move right
def right():
	m.right(player)

# move forward
def forward():
	m.forward(player)

# move backward
def backward():
	m.backward(player)

# print character health, attack, armor and healtlimit
def print_character_values():
	print("Health: ", player.hp)
	print("Attack/Damage: ", player.attack)
	print("Armor (Damage decrease): ", player.armor)
	print("Healthbarlimit: ", player.hp_limit)

# print inventar
def print_inventar():
	for i in inventar.inventar_print:
		print(i)

# print the information about all items
def get_item_info():
	print("These are the following Items:")	
	for i in m.items:
		print(i)

	print("\n")
	time.sleep(1)
	print("HP- stands for Healpotion and heal 50 hp")
	time.sleep(1)
	print("AP- stands for Attackpotion and increas your attack by 50 attack")
	time.sleep(1)
	print("S1- stands for Sword-1 and increase you attack by 20 attack (only equip 1), with every level you can collect better Swords which increases your attack more")
	time.sleep(1)
	print("A1- stands for Armor-1 and decrease your damage by monster by 5 and increases your healtbarlimit by 30(quip up to 8), same concept as by Sword, every level got better armor")

# player using a item
def use_item():
	inventar.use_item(m.items, player)

# Commands the player can select
Commands = {
	"help": print_Commands,
	"print_map": print_map,
	"print_position": print_position,
    "left": left,
    "right": right,
    "forward": forward,
    "backward": backward,
    "print_character_values": print_character_values,
    "print_inventar": print_inventar,
    "get_item_info": get_item_info,
    "use_item": use_item
}

class LevelOne():
	def __init__(self):
		print("\n<----------------------------------------------------------------------------------------------------------------------------->")
		print("<----------------------------------------------------<-Level 1->-------------------------------------------------------------->")
		print("<----------------------------------------------------------------------------------------------------------------------------->\n")

		
		while True:
			command = input("~ ").lower()
			if command in Commands:
				print("")
				Commands[command]()
				print("")
			elif command == "quit":
				break
			else:
				print("Oh no, this command doesen´t exist :/\n Try again")

			if m.item != "":
				for i in range(len(inventar.inventar_list)):
					if inventar.inventar_list[i] == "---":
						inventar.inventar_list[i] = m.item
						inventar.reload()
						break
				m.item = ""

			if m.next_level == True:
				break