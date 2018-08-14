"""Script to create a report of PDF's created (scanned) by day"""

import sys
import os
import platform
import time
import json
from PyPDF2 import PdfFileReader

directory = "C:/Users/rchejf/Documents/Scanned Documents/"
#directory = "/Users/ricardochejfec/Documents/School/Anthropology/ANTH 540/Readings/"

def main():
	
	###### Testing in Mac
	#files = ["jonathan.pdf", "positive sexual wellbeing.pdf", "Sexual Pleasure and Wellbeing.pdf"]
	######
	
	files = []
	for filename in os.listdir(directory):
		files.append(filename)

	master_dict = create_master_dictionary(files)
	print(master_dict)
	pass

def create_master_dictionary(list_of_files):
	"""Iterate through all files and create a dictionary containing by date: 
	# of documents,
	# of pages,
	first document of the day
	last document of the day """

	# for filename in os.listdir(directory):
	# 	filename_full = directory + filename
	# 	file = open(filename_full, "rb")

	master_dict = {}
	master_dict["Files"] = []
	
	for filename in list_of_files:
		filename_full = directory + filename
		file = open(filename_full, "rb")

		date_created_full = time.ctime(os.path.getctime(filename_full)).split(" ")
		
		# Windows! 
		date_created = " ".join([date_created_full[i] for i in [0,2,1,4]])
		time_created = date_created_full[3]

		# Mac! 
		# date_created = " ".join([date_created_full[i] for i in [0,3,1,5]])
		# time_created = date_created_full[4]
			
		

		if filename not in master_dict["Files"]:
			master_dict["Files"].append(filename) 
		 
			if date_created in master_dict:
				master_dict[date_created]["Documents"] += 1
				master_dict[date_created]["Pages"] +=  PdfFileReader(file).getNumPages()

				if (calculate_time_in_between(master_dict[date_created]["First"], time_created) <= 0):
					master_dict[date_created]["First"] = time_created

				if (calculate_time_in_between(master_dict[date_created]["Last"], time_created) > 0):
					master_dict[date_created]["Last"] = time_created
		    
			else:
				master_dict[date_created] = {}
				master_dict[date_created]["Documents"] = 1 
				master_dict[date_created]["Pages"] =  PdfFileReader(file).getNumPages()
				master_dict[date_created]["First"] = time_created
				master_dict[date_created]["Last"] = time_created
	
			master_dict[date_created]["Hours"] = calculate_time_in_between(master_dict[date_created]["First"], master_dict[date_created]["Last"])

	return master_dict

def calculate_time_in_between(time1, time2):

	start_time = int(time1.split(":")[0]) * 60 + int(time1.split(":")[1])
	end_time = int(time2.split(":")[0]) * 60 + int(time2.split(":")[1])

	return (end_time - start_time)/60.0

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