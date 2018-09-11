class EmptyDarknes(object):
	
	def enter(self):
		print "you skipped the door carefully, it's another room! you turned your head around to see whats there, on your left there is a dead cat ,maybe a savage animal have killed it."
		print "wait some thing is coming ......\"agh ahg agh\"  its a zombie coming after you !"
		return 'zombie attack'
		
class ZombieAttack(object):
	
	def enter(self):
		rep = [
		"while you are runing for your life the zombie was able to get closer to you and kill you !",
		"You just did a head shot, the zombie is dead!"
		]
		
		for i in range(0,10):
			print "what will you do ?"
			answer = raw_input("{Run, Shot the zombie} > ")
			if answer == 'run':
				print rep[0]
				exit(1)
				
			elif answer == 'shot the zombie':
				print rep[1]
				print "look what you found in his pocket its the main door key!, so you go to the main door and open it \nCongratulations you escaped :D"
				exit(1)
				
			else:
				print "I can't understand"
		
