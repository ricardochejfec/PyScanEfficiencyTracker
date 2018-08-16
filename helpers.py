

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


def format_day_log(key, day_stats):
	retrun "<tr><td>key</td><td>day_stats["Hours"]</td><td>day_stat["Documents"]</td><td>day_stats["Pages"]</td><td>day_stats["PagesPerDocument"]</td><td>day_stats["PagesPerHour"]</td></tr>