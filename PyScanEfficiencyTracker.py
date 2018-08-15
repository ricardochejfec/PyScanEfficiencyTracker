import sys 
import os 
import time
from PyPDF2 import PdfFileReader

def main(args):
	directory_in = args[0]
	directory_out = args[1]
	file_out_name = args[2] 

	master_dict = track_pages(directory_in)
	create_report(directory_out, master_dict, file_out_name) 
	#(exit)

def track_pages(directory_in):
	
	for filename in os.listdir(directory):

		master_dict = {} 

		if helpers.is_pdf(filename):

			filename_full = directory_in + filename
			file = open(filename_full, "rb")

			date_created_full = time.ctime(os.path.getmtime(filename_full)).split(" ")
		
			# Windows! 
			date_created = " ".join([date_created_full[i] for i in [0,2,1,4]])
			time_created = date_created_full[3]

			# Mac! 
			# date_created = " ".join([date_created_full[i] for i in [0,3,1,5]])
			# time_created = date_created_full[4]
		 
			if date_created in master_dict:
				master_dict[date_created]["Documents"] += 1
				master_dict[date_created]["Pages"] +=  PdfFileReader(file).getNumPages()

				if (helpers.calculate_time_in_between(master_dict[date_created]["First"], time_created) <= 0):
					master_dict[date_created]["First"] = time_created

				if (helpers.calculate_time_in_between(master_dict[date_created]["Last"], time_created) > 0):
					master_dict[date_created]["Last"] = time_created
		    
			else:
				master_dict[date_created] = {}
				master_dict[date_created]["Documents"] = 1 
				master_dict[date_created]["Pages"] =  PdfFileReader(file).getNumPages()
				master_dict[date_created]["First"] = time_created
				master_dict[date_created]["Last"] = time_created
	
			master_dict[date_created]["Hours"] = calculate_time_in_between(master_dict[date_created]["First"], master_dict[date_created]["Last"])

	return master_dict

def create_report():
	pass


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))