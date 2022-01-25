from map import Level_1
from player import *
from inventar import *
import time

m = Level_1()
player = Player(1)
inventar = Inventar()

def print_Commands():
	for index, cmd in enumerate(Commands):
		if index < 10:
			print(index, " ->", cmd)
		else:
			print(index, "->", cmd)

def print_map():
	m.print_map()

def print_position():
	print(m.x, ", ",m.y)

def left():
	m.left()

def right():
	m.right()

def forward():
	m.forward()

def backward():
	m.backward()

def fight():
	pass

def print_hp():
	print(player.hp)

def print_character_values():
	print("Health: ", player.hp)
	print("Attack/Damage: ", player.attack)
	print("Armor (Damage decrease): ", player.armor)
	print("Healthbarlimit: ", player.hp_limit)

def print_inventar():
	for i in inventar.inventar_print:
		print(i)

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

def use_item():
	inventar.use_item(m.items, player)

def get_monster_info():
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
    "use_item": use_item,
    "get_monster_info": get_monster_info
}

class Level_1():
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