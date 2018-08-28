import sys
import os
import platform 
from pprint import pprint
import PyScanEfficiencyTracker
import itertools
import threading
import json
import time

done = False 

#directory_in = "G:/PROVOST/Share/OAP/BR/Professional Development Fund/CRC Scanning July 2018/"
#directory_in = "/Users/ricardochejfec/Documents/School/Anthropology/ANTH 540/Readings/"

#directory_in = "C:/Users/rchejf/Documents/Scanned Documents/"

def main(args):
	
	if args:
		if args[0] == "-w":
			directory_in = "G:/PROVOST/Share/OAP/BR/Professional Development Fund/CRC Scanning July 2018/"
		elif args[0] == "-t":
			directory_in = "C:/Users/rchejf/Documents/Scanned Documents/"
		elif args[0] == "-tm":
			directory_in = "/Users/ricardochejfec/Documents/School/Anthropology/ANTH 540/Readings/"
	else:
		directory_in = "G:/PROVOST/Share/OAP/BR/Professional Development Fund/CRC Scanning July 2018/"
		
	#----------Animation
	global done
	print("")
	t = threading.Thread(target=animate)
	t.daemon = True
	t.start()
	#----------

	#----------Efficiency
	try:
		with open("master_data.json", "r") as f:
			master_data = json.load(f)
	except:
		master_data = {}
	#----------
	
	master_dict = PyScanEfficiencyTracker.track_pages(directory_in, master_dict = master_data)
	#pprint(master_dict)
	PyScanEfficiencyTracker.create_report(master_dict)  

	with open("master_data.json", "w") as f:
			json.dump(master_dict, f)
	
	time.sleep(1)
	done = True
	time.sleep(1)
	print("")

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
	

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))