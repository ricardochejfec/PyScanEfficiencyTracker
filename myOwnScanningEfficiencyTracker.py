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

dir1 = "C:/blah/blah"
dir2 = "C:/blah/blah"
dir3 = "C:/blah/blah"

def main(args):
	
	if args:
		if args[0] == "-w":
			directory_in = dir1
		elif args[0] == "-t":
			directory_in = dir2
		elif args[0] == "-tm":
			directory_in = dir3
	else:
		directory_in = "C:/blah/blah"
		
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
