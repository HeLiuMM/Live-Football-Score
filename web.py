import bs4,requests
import URLS,CLI
from Message import sendmessage


def Score(soup):
	tag_name=soup.select(".name")
	tag_score=soup.select(".sco")
	tag_minute=soup.select(".min")
	tag_time=soup.select(".fs11")
	print "\n\n"
	for i in range(len(tag_score)):
		print "{:<2}{} {:<23}{:<18}{} ".format(i+1,tag_minute[i].text,tag_name[2*i].text,tag_score[i].text,tag_name[(2*i) +1].text)
		
#### {:<4} means that 4 spaces will be left from the FIRST character of the string being printed
def Table(soup):
	team_name=soup.select(".team")
	team_points=soup.select(".pts")
	for i in range(len(team_name)):
		temp=''
		for j in range(8):
			temp+="{}\t".format(team_points[(8*i) +j].text).expandtabs(5)
			temp+=" "
		if i==0:
			print "\n\nNo.  {:<20} {:<20}".format(team_name[i].text,temp).expandtabs(3)
		else:
			print "{}.\t {:<20} {:<20}".format(i,team_name[i].text,temp).expandtabs(2)


def Message_Score(choice,soup):
	tag_name=soup.select(".name")
	tag_score=soup.select(".sco")
	tag_minute=soup.select(".min")
	tag_time=soup.select(".fs11")
	if choice==0:
		for i in range(len(tag_score)):
			a= "{}\t{}  {}  {} ".format(tag_minute[i].text,tag_name[2*i].text,tag_score[i].text,tag_name[(2*i) +1].text)
			sendmessage(a)
	else:
		i=choice-1
		a= "{}\t{}  {}  {} ".format(tag_minute[i].text,tag_name[2*i].text,tag_score[i].text,tag_name[(2*i) +1].text)
		sendmessage(a)