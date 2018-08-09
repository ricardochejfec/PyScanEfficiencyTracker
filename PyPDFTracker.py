"""Script to create a report of PDF's created (scanned) by day"""

import sys
import os
import platform
import time
from pyPdf import PdfFileReader

directory = "C:/Users/rchejf/Documents/Scanned Documents/"

def main():
    """Main entry point for the script."""
    pass


def create_master_dictionary(list_of_files):
    """Iterate through all files and create a dictionary containing by date: 
	# of documents,
	# of pages,
	first document of the day
	last document of the day 
	"""
    
    master_dict = {}

    for filename in os.listdir(directory):
	
        filename_full = directory + filename
	file = open(filename_full, "rb)

	date_created_full = time.ctime(os.path.getctime(filename_full)).split(" ")
	date_created = " ".join([date_created_full[i] for i in [0,2,1,4]])
	time_created = date_created_full[3]

	master_dict[date_created] = master_dict.get(date_created, {})

	if date_created in master_dict:
            master_dict[date_created]["Documents"] += 1 
	    master_dict[date_created]["Pages"] +=  PdfFileReader(file).getNumPages()
	    
	    if compare_time(master_dict[date_created]["First"], time_created):
		master_dict[date_created]["First"] = time_created

	    if not compare_time(master_dict[date_created]["Last"], time_created):
		master_dict[date_created]["Last"] = time_created
	    
	else:
	    master_dict[date_created] = {}
	    master_dict[date_created]["Documents"] = 1 
	    master_dict[date_created]["Pages"] =  PdfFileReader(file).getNumPages()
	    master_dict[date_created]["First"] = time_created
	    master_dict[date_created]["Last"] = time_created

    return master_dict

def compare_time(time1, time2):
	if (time1.split(":")[0] > time2.split(":")[0]):
		return True 
	elif (time1.split(":")[0] < time2.split(":")[0]):
		return False 
	elif (time1.split(":")[1] > time1.split(":")[1]):
		return True 
	elif (time1.split(":")[1] < time1.split(":")[1]):
		return False 
	elif (time1.split(":")[2] >= time1.split(":")[2]):
		return True
	else: 
		return False 
	


def calculate_totals(master_dict):
    """Calculate:
	- total hours 
	- total documents
	- total pages 
	- hours per day
	- efficiency per day"""
    pass

def create_report(master_dict): 
     """create a report in markdown into an html file and open it"""
    pass


if __name__ == '__main__':
    sys.exit(main())