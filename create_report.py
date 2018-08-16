import webbrowser 


def processStats(list_of_workdays):
	total_hours = 0
	total_documents = 0
	total_pages = 0 
	most_efficient_day = ""
	most_efficient_rate = 0 
	str_workdays = "" 
	
	for key in sorted(list_of_workdays):
		workday =  str(key) + " - " + formatDictEntry(list_of_workdays[key])
		str_workdays += workday + "<br>"
		total_hours += list_of_workdays[key]["Hours"]
		total_documents += list_of_workdays[key]["Documents"]
		total_pages += list_of_workdays[key]["Pages"]
		if (list_of_workdays[key]["PagesPerHour"] > most_efficient_rate):
			most_efficient_rate = list_of_workdays[key]["PagesPerHour"]
			most_efficient_day = workday
			
	html_str = createHTMLStr(total_hours, total_documents, total_pages, most_efficient_day, str_workdays)
	
	f = open("efficient_scanning_report.html", "w")
	f.write(html_str)
	f.close()
	filename = "C://Users/rchejf/Documents/Efficient Scanning/efficient_scanning_report.html"
	webbrowser.open(filename)


def formatDictEntry(day_stats): 
	result = ""
	for c, v in day_stats.iteritems():
		result += str(c) + ": " + str(v) + " | "
	return result


def createHTMLStr(hours, documents, pages, best_day, workdays):
	basic_content = "<html><head></head><body><h1>Efficient Scanning Report</h1><h3>Hours Worked: {0}</h3><h3>Documents Scanned: {1}</h3><h3>Pages Scanned: {2}</h3><h3>Average Rate: {3} pages per hour</h3><h3>Average Document: {4} pages long</h3><p><h3>Best Day:</h3>{5}</p><p><h3>Log:</h3> {6} </p></body></html>".format(hours, documents, pages, round((pages/hours), 2), (pages/documents), best_day, workdays)
	return basic_content