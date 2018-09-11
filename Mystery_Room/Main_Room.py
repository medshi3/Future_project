""" =====================IMPORTING THE OTHER CLASSES TO USE FROM THE OTHER FILE============================"""
from Zombie_Room import EmptyDarknes
from Zombie_Room import ZombieAttack
from random import randint
import time

"""======================THE ENGINE THAT WILL RUN THE GAME============================="""
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
	
	# the time.sleep() is to print the text after a certain time 
class Begining(object):

	def enter(self):
		print "You wake up!, in a complete Dark room"
		time.sleep(1.5)
		print "you don't know what happen , you don't remember anything"
		time.sleep(1.5)
		print "wait there is a candle in the corner of the room."
		time.sleep(1.5)
		rep = {
			'scream': "I think this will not help you\n",
			'take the candle': "Good choice\n"
			}
		
		for i in range (0,30):
			answer = raw_input('what will you do? [scream, take the candle] \n=> ')
			if answer == 'take the candle':
				print rep['take the candle']
				time.sleep(1.5)
				print "now the vision is a bit clear you can take a tour on the room, you go forward you see an ancien chest"
				time.sleep(1.5)
				print "you tried to open it but its locked you need a key to open it, look there is a painting in the other wall"
				time.sleep(1.5)
				print "so you keep walking and its in front of you "
				return 'the painting'
				
			elif answer == 'scream':
				print rep['scream']
			
			else:
				print "this wont help you !"
				
		
class ThePainting(object):
	
	def enter(self):
		print "some thing suspicious about this painting"
		rep = {
			'move it': "Yikes look what we find!",
			'do nothing': "Really in the middle of no where and just do nothing -_- "
			}
			
		for i in range (0,30):
			answer = raw_input("what will do to the painting? [move it, do nothing] => ")
			if answer == 'move it':
				rep['move it']
				print "There is a money safe in the wall and it has a KeyPad, lets try to guess the code!"
				code = "%d%d%d%d" %(randint(1,9), randint(1,9), randint(1,9), randint(1,9))
				guess = raw_input("[keypad] ' you need 4 numbers '> ")
				guesses = 0
				
				while guess != code and guesses < 20:
					print"BZZZZEDDD!"
					guesses += 1
					if guesses == 3:
						print code
					guess = raw_input("[keypad]> ")
					
				if guess == code :
					print "Yesss! you open it :D, by moving the candle into the money safe you find a key and an empty gun!"
					time.sleep(1.5)
					print "so you just take them and try to open the chest"
					return 'the chest'
					
			elif answer == 'do nothing':
				rep['do nothing']
				
			else:
				print "Write something helpfull -_-"
		
class TheChest(object):

	def enter(self):
		print "You move back to the chest with the in you hand, as you put the key in the chest and turn it around it does open up"
		time.sleep(1.5)
		print "You find the Door key and 3 bullets, so you take them and you go straight forward to the door!"
		return 'door'
		
class Door(object):
	
	def enter(self):
		print "you are so happy because you are going to leave this room, so you put the key into the door, but it doesn't open! but look there is a small window open in the door and it has another keypad like in the money safe"
		time.sleep(2.5)
		code = "%d%d" %(randint(1,2), randint(2,3))
		guess = raw_input("[KeyPad] ' you need 2 numbers ' > ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print"BZZZZEDDD!"
			guesses += 1
			if guesses == 3:
				print code
			guess = raw_input("[keypad]> ")
			
		if guess == code :
			print "Yes you did it you open the door, you walk forward in the outside of the room there is like a tunnel"
			print "so you keep walking till you find another door at the end of the tunnel, but this door is open!"
			return 'empty darknes'
			
"""============================ THE MAP THAT THE ENGINE WILL USE IT ==========================="""	
class Map(object):
	
	scenes = {
		'begining': Begining(),
		'the painting': ThePainting(),
		'the chest': TheChest(),
		'door': Door(),
		'empty darknes': EmptyDarknes(),
		'zombie attack': ZombieAttack()
		}
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return self.scenes[scene_name]
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('begining')
a_game = Engine(a_map)
a_game.play()