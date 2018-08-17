import sys 
import os 
import time
from PyPDF2 import PdfFileReader
import helpers
import webbrowser 

def main(args):
	directory_in = args[0]
	directory_out = args[1]
	file_out_name = args[2] 

	master_dict = track_pages(directory_in)
	create_report(directory_out, master_dict, file_out_name) 
	#(exit)

def track_pages(directory_in, master_dict = {}):
	
	for filename in os.listdir(directory_in):

		if helpers.is_pdf(filename):
			filename_full = directory_in + filename
			file = open(filename_full, "rb")

			date_created_full = time.ctime(os.path.getmtime(filename_full)).split(" ")
		
			# Windows! 
			# date_created = " ".join([date_created_full[i] for i in [0,2,1,4]])
			# time_created = date_created_full[3]

			# Mac! 
			date_created = " ".join([date_created_full[i] for i in [0,3,1,5]])
			time_created = date_created_full[4]
		 
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
			file.close()
	
			master_dict[date_created]["Hours"] = helpers.calculate_time_in_between(master_dict[date_created]["First"], master_dict[date_created]["Last"])

	return master_dict

def create_report(directory_out="", master_dict, file_out_name="Scanning Efficiency Report"):
	
	total_hours = 0
	total_documents = 0
	total_pages = 0 
	most_efficient_day = ""
	most_efficient_rate = 0
	
	overall_stats = "" 
	today_stats = "" 
	recent_day_log = "" 

	html_str = ""

	for key in sorted(list_of_workdays):
		workday = helpers.format_day_log_entry(key, list_of_workdays[key])
		day_log += workday 

		total_hours += list_of_workdays[key]["Hours"]
		total_documents += list_of_workdays[key]["Documents"]
		total_pages += list_of_workdays[key]["Pages"]
		if (list_of_workdays[key]["PagesPerHour"] > most_efficient_rate):
			most_efficient_rate = list_of_workdays[key]["PagesPerHour"]
			most_efficient_day = helpers.format_best_day(key, list_of_workdays[key])

	recent_day = sorted(list_of_workdays,reverse="True")[0]
	recent_day_log = helpers.format_recent_stats(list_of_workdays[recent_day]["Hours"],list_of_workdays[recent_day]["Documents"],list_of_workdays[recent_day]["Pages"])

	overall_stats = helpers.format_overall_stats(total_hours, total_documents, total_pages)
	html_str = format_html_str(overall_stats,today_stats,day_log)

	f = open("efficient_scanning_report.html", "w")
	f.write(html_str)
	f.close()
	filename = "C://Users/rchejf/Documents/Efficient Scanning/efficient_scanning_report.html"
	webbrowser.open(filename)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))