import subprocess,os

def sendmessage(message):
	icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"livescore.png")
	title="Live Score"       
    #bash command to send notification 
	# bash_command = 'notify-send -i '+icon_path+message
	# print message
	bash_command = 'notify-send -i '+icon_path+' "'+title+'" "'+message+'"'
	os.system(bash_command)
	return
    # subprocess.Popen(['notify-send', message])
    # return

