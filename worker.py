import requests
import os
import os.path
import sys
import time
import threading

version = 20160417.01

def main():
	while True:
		if os.path.isfile("./STOP") == true:
			# Wait 2 Hours before exiting, so all remaining processes can finish
			time.sleep(7200)
			sys.exit()
		new_script = requests.get('https://raw.githubusercontent.com/ArchiveTeam/NewsGrabber/master/worker_script.py')
		if new_script.status_code == 200 and len(new_script.text) > 0:
			with open('worker_script.py', 'w') as file:
				file.write(new_script.text)
			threading.Thread(target = grab).start()
		else:
			print('Something went wrong. How is your internet connection?')
		time.sleep(300)

def grab():
	returned = os.system('python worker_script.py')
	if returned != 0:
		print('Something went wrong running this script.')

if __name__ == '__main__':
	main()
	
