

def is_pdf(filename):
	try: 
		if filename[-3:] == "pdf":
			return True
		else:
			return False 
	except:
		return False


def calculate_time_in_between(time1, time2):

	start_time = int(time1.split(":")[0]) * 60 + int(time1.split(":")[1])
	end_time = int(time2.split(":")[0]) * 60 + int(time2.split(":")[1])

	return (end_time - start_time)/60.0


def format_day_log_entry(key, day_stats):
	return """<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>""".format(key,day_stats["Hours"], day_stats["Documents"], day_stats["Pages"], round(float(day_stats["Pages"])/day_stats["Documents"],3), round(float(day_stats["Pages"])/day_stats["Hours"],3))

def format_best_day(key, day_stats):
	return "{} <br> {} hours - {} documents - {} pages, <br> {} pages/document -- {} pages/hour.".format(key, day_stats["Hours"],day_stats["Documents"],day_stats["Pages"],round(float(day_stats["Pages"])/day_stats["Documents"],3), round(float(day_stats["Pages"])/day_stats["Hours"],3))

def format_recent_day(hours,documents,pages):
	return """<div id="today"><h3>Today:</h3><div id="today-text"> Hours: <br> {} <br> Documents: <br> {} <br> Pages Scanned: <br> {} <br> Pages/Document: <br> {} <br>Pages/Hour: <br> {} <br></div></div>""".format(hours, documents, pages, round(float(pages)/documents,3), round(float(pages)/hours)) 

def format_overall_stats(hours,documents,pages, bestday):
	return """<div id="all-stats">
			<h3>Hours Worked:</h3> {}
			<h3>Documents Scanned:</h3>{}
			<h3>Pages Scanned: </h3> {}
			<h3>Average Rate: </h3> {} pages/hour
			<h3>Average Document:</h3> {} pages long
			<p>
			<h3>Best Day:</h3>
			{}</div>""".format(hours, documents, pages, round(float(pages)/documents,3), round(float(pages)/hours, 3), bestday)


def format_html_str(overall_stats,today_stats,day_log):
	return """<html>
	<head>
		<style>
			body {background-color: whitesmoke;margin:0;padding:30}
			h1   {color: ;}
			p    {color: red;}
			#title {text-align: center;}
			#all-stats {border: solid 1px black; padding: 20px 80px; width: 60%; text-align: center; margin: 0 auto;}
			#day-log {grid-column: 1 / span 2; padding: 20px; margin: 0 auto; column-width: 20px;}
			#today {border: solid 1px black; padding:20px 60px; width: 40%; text-align: center; margin: 0 auto;}
			#today-text {line-height: 40px;}	
			#grid-container {display: grid; justify-content: space-evenly; grid-gap: 20px; grid-template-columns: 40% 60%; grid-template-rows: 30% 70%}
			th, td {padding: 10px; text-align: center; border-bottom: 1px dotted black}
		</style>
	</head>
	<body>
		<h1 id="title">Efficient Scanning Report</h1>
	<div id="grid-container">
		{}
		{}
		<div id="day-log" style="display:table">		
			<table id="DayLogTable">
				<tr>
				<th>Date</th>
				<th>Hours</th>
				<th>Documents</th>
				<th>Pages</th>
				<th>Pages per Document</th>
				<th>Pages per Hour</th>
				</tr>
				{}
			</table></div></div></body></html>""".format(today_stats, overall_stats, day_log)
 