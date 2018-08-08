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
    
    for filename in os.listdir(directory):
	master_dict = {}
        filename_full = directory + filename
	date_created_full = time.ctime(os.path.getctime(filename_full)).split(" ")
	date_created = " ".join([date_created_full[i] for i in [0,2,1,4]])
	time_created = date_created_full[3]
	 
	
    pass

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