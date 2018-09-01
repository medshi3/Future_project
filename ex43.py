"""
* Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
"""
from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subcalss it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		
class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
		]
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
			
class Battle(object):
	
	def __init__(self):
		player_hp = 5000
		monster_hp = 200
		self.player_hp = player_hp
		self.monster_hp = monster_hp
		
	def enter(self):
		print "you find a big large monster trying to kill you what will you do !"
		print "The monster is coming to you harry up!"
		
		for i in range (0,30):
			answer = raw_input("[Defend, Attack] > ")
			answer_1 = answer.capitalize()
			if answer_1 == 'Defend':
				self.player_hp -= randint(500,1000)
				if self.player_hp > 0:
					print "The monster have did some damage to you! here is your hp:", self.player_hp
					print "I guess you will try the other solution cause you are not doing any damage to him! 'monster hp: '", self.monster_hp
				elif self.player_hp <= 0:
					print "I guess you are stupid  you are dead now !"
					print "Your Hp is : 0"
					print "Such a Mother Fucking loser :)"
					break
					
			
			elif answer_1 == 'Attack':
				self.player_hp -= randint(50,200)
				self.monster_hp -= randint(50,100)
				if self.player_hp > 0 and self.monster_hp > 0:
					print "\n--------"
					print "I think its working lets keep going"
					print "Your Hp: ", self.player_hp 
					print "Monster Hp:", self.monster_hp
				elif self.player_hp > 0 and self.monster_hp <= 0:
					print "Yes you have defeted the monster"
					print "Your Hp: ", self.player_hp 
					print "the Monster HP: 0"
					print "Great Bitch You win! :p"
					break
					
			else:
				print"Sorry didn't understand"
					

		
		
class CentralCorridor(Scene):
	
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You should do some thing to escape from them \n there is a fagget over there trying to kill you, what will you do?"
		print "[shoot!, dodge!, tell a joke]"
			
		action = raw_input("> ")
			
		if action == "shoot!":
			print "Do you realy expect to kill him he is too fast! he run to you and killed you."
			return 'death'
				
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "he got a shoot on you and you died"
			return 'death'
				
		elif action == "tell a joke":
			print "You lucky you Good at thoese idiots Language so you tell them: \n Suck Ma Dick!\n and just like that you escaped."
			return 'laser_weapon_armory'
				
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
				
	
class LaserWeaponArmory(Scene):
	
	def enter(self):
		code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9))
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits \" the Code:\"",code 
		
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 9:
			print"BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
		
class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		print "{throw the bomb, slowly place the bomb}"
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
			
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
		
class EscapePod(Scene):
	
	def enter(self):
		code = randint(1,5)
		print "Where the hero escapes but only after guessing the right escape pod.", code
		
		
		guess = int(raw_input("[pod #]> "))
		
		if guess == code:
			print "You just finish the game yay!"
			print "Oh wait there is some in in the room!"
			return 'battle'
			
		else:
			print "You have field"
			return 'death'
		
class Map(object):
	
	scenes = {
		'battle': Battle(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'central_corridor': CentralCorridor(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return self.scenes[scene_name]
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()