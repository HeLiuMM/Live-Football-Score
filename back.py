from web import Table,Score
import requests,bs4
list_league=["Barclays Premiere League","Serie-A","Bundesliga","LaLiga","Ligue-1"]
		
def ask_user(soup):
	print "\n\n\n\n\nWhich match do you want to see live notifications for?"
	while True:
		try:
			which_match=int(raw_input())
			tag_name=soup.select(".name")
			print "You will get the notifications for{}vs{} \n".format(tag_name[2*(which_match-1)].text,tag_name[2*(which_match-1) +1].text)

			return which_match
		except:
			print "Please enter the correct match number."

def Choose_League():
	print "Which league do you want to get the score of?"
	for count,name in enumerate(list_league):
		print "{}. {}".format(count+1,name)

	while 1:
		try:
			while 1:
				league=int(raw_input("Enter the corresponding number\n"))
				if league not in range(0,len(list_league)):
					print "Please correct input"
				else:
					return(league)
		except:
			print "Please correct input"

def Score_or_Table_or_Both():
	print """Enter the number next to the option you want:
1. The score of the ongoing matches in the league.
2. The table of the league.
3. The table as well as the score. """
	while 1:
		try:
			while 1:
				option=int(raw_input())
				if option not in [1,2,3]:
					print "Please enter a valid choice"
				else:
					print "Please wait while we fetch the data for you"
					return option
		except:
			print "Please enter a valid choice"

#This decides what data to display based on the user's entry
def Selected_Choice(option,soup):
	if option==1:
		Score(soup)
		which_match=ask_user(soup)
		time=interval()
		return which_match,time
	elif option==2:
		Table(soup)
		return False,1
	else:
		Table(soup)
		Score(soup)
		which_match=ask_user(soup)
		time=interval()
		return which_match,time

def interval():
	print "Please enter the Time Period for the Live Notifications on your system (In Seconds)"
	while 1:
		try:
			time=int(raw_input())
			return time
		except:
			print "Please enter an Integer"