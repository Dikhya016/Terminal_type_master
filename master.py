import keyboard as kb
from random_word import RandomWords as RW
from time import time, sleep
from threading import Thread

r=RW()

def showLeaderBoard():
	global all_players
	sleep(2)
	print()
	print('NAME\t\tWORDS\t\tTIME(sec)\tWPM')
	print('='*60)
	for p1 in all_players:
		print('{}\t\t{}\t\t{}\t\t{}'.format(p1.name,p1.words,p1.playtime,p1.wpm))
	
def monitorForQuit(p1):
	global end_flag,all_players
	while(True):
		if(kb.is_pressed('ctrl+q')):
			#print('User tried to quit')
			end_flag=1
			break
		
	p1.end_time=time()
	p1.playtime=int(p1.end_time-p1.start_time)
	p1.wpm=p1.words*60//p1.playtime

	showLeaderBoard()		

def getUserInput(p1):
	global end_flag
	print('Start typing the word shown to you. Press Ctrl+Q to exit')
	p1.start_time=time()
	while(True):
		
		if(end_flag==1):
			print('Your turn finished !!')
			break

		word=r.get_random_word()

		user_inp=''

		while(user_inp != word):
			print(word)
			user_inp=input()
			if(user_inp == word):
				print('correctly typed')
				p1.words+=1
			else:
				if(end_flag==0):
					print('Incorrectly typed word !! Type again')
				else:
					break
		print()


class Player:
	def __init__(self,name):
		self.name=name
		self.words=0
		self.start_time=0
		self.end_time=0
		self.wpm=0


all_players=[]
game_run=1
while(game_run):

	end_flag=0

	player=input('Enter your name : ')
	p1=Player(player)
	all_players.append(p1)
	
	t1=Thread(target=getUserInput,args=(p1,))
	t1.start()


	t2=Thread(target=monitorForQuit,args=(p1,))
	t2.start()

	t1.join()
	t2.join()

	print()
	print('1. Play another game')
	print('2. Quit game')
	option=input('Enter your option : ')

	if(option=='2'):
		game_run=0
	elif(option=='1'):
		pass
	else:
		print('You have entered invalid option.')
		print('Game will end')
		break
	print()
