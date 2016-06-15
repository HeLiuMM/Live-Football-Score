from bs4 import BeautifulSoup
from URLS import URLS as url
from Message import sendmessage
from back import ask_user
from web import Table
from web import Score
from web import Message_Score
from time import sleep
from back import Choose_League,Selected_Choice,Score_or_Table_or_Both

import requests,threading,sys,os

def all():
	league=Choose_League()
	option=Score_or_Table_or_Both()
	req=requests.get(url[league-1])
	soup=BeautifulSoup(req.text,"html.parser")
	global which_match
	which_match,time=Selected_Choice(option,soup)

	e.set()

	if which_match:
		while 1:
			if which_match==0:
				sys.exit()
			Message_Score(which_match,soup)
			sleep(time)
	else:
		sys.exit()

def choice_exit_changeteam(e):
	event_is_set=e.wait()
	global which_match
	if which_match==False:
		sys.exit()

	print """Enter zero to exit
Or if you want to see the score of some other match,then enter the number"""
	while 1:
		try:
			inp=int(raw_input())

			if inp==0:
				which_match=0
				# sys.exit()
				break
			elif inp in range(1,15):		#Change it to the actual number of matches
				which_match=inp
				print """Enter 0 to exit
Or if you want to see the score of some other match,then enter the number"""
			else:
				print "Invalid Choice"
		except:
			print "Invalid Choice"
		if which_match==0:
			sys.exit()
which_match=0
e = threading.Event()
t1 = threading.Thread(target=all)
t1.setDaemon(True)

t1.start()
t2=threading.Thread(target=choice_exit_changeteam,args=(e,))
# sleep(3)
t2.start()
# logging.debug('Waiting before calling Event.set()')
# time.sleep(3)
# logging.debug('Event is set')