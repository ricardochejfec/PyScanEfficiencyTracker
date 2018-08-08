"""Script to create a report of PDF's created (scanned) by day"""

import sys
import os 
import json
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