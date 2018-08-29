

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

def month_switch(month):
	switcher = {
		"Jan":0,
		"Feb":40,
		"Mar":80,
		"Apr":120,
		"May":160,
		"Jun":200,
		"Jul":240,
		"Aug":280,
		"Sep":320,
		"Oct":360,
		"Nov":400,
		"Dec":440
	}
	return switcher.get(month, "invalide month")

def sorting_helper(date):
	new_date = date.split(" ")
	result = int(new_date[1]) + month_switch(new_date[2]) + int(new_date[3])*1000
	return result

def deconstruct_day(day_stats):
	if day_stats["Hours"] > 0:
		return [round(day_stats["Hours"],2), day_stats["Documents"], day_stats["Pages"], round(float(day_stats["Pages"])/day_stats["Documents"],3), round(float(day_stats["Pages"])/day_stats["Hours"],1)]
	else:
		return[round(day_stats["Hours"],2), day_stats["Documents"], day_stats["Pages"], round(float(day_stats["Pages"])/day_stats["Documents"],3), 0]

def format_day_log_entry(key, day_stats):
	day_as_list = deconstruct_day(day_stats)
	return """<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>""".format(key, day_as_list[0], day_as_list[1], day_as_list[2], day_as_list[3], day_as_list[4])

def format_best_day(key, day_stats):
	day_as_list = deconstruct_day(day_stats)
	return """{} <br> {} hours - {} documents - {} pages, <br> {} pages/document -- {} pages/hour.""".format(key, day_as_list[0], day_as_list[1], day_as_list[2], day_as_list[3], day_as_list[4])

def format_recent_day(hours,documents,pages):
	if hours == 0:
		hours = 0.1
	return """<div id="today"><h3>Today:</h3><br><div id="today-text"> Hours: <br> {} <br> Documents: <br> {} <br> Pages: <br> {} <br> Pages/Document: <br> {} <br>Pages/Hour: <br> {} <br></div></div>""".format(round(hours,2), documents, pages, round(float(pages)/documents,3), round(float(pages)/hours)) 

def format_overall_stats(hours,documents,pages, bestday):
	return """<div id="all-stats">
			<h3>Hours Worked:</h3> {}
			<h3>Documents Scanned:</h3>{}
			<h3>Pages Scanned: </h3> {}
			<h3>Average Document: </h3> {} pages
			<h3>Average Rate:</h3> {} pages/hour
			<p>
			<h3>Best Day:</h3>
			{}</div>""".format(round(hours,2), documents, pages, round(float(pages)/documents,1), round(float(pages)/hours, 1), bestday)


def format_html_str(overall_stats,today_stats,day_log):
	return """<html>
	<head>
		<style>
			body {{background-color: whitesmoke;margin:0;padding:30}}
			h1   {{color: ;}}
			p    {{color: red;}}
			#title {{text-align: center;}}
			#all-stats {{border: solid 1px black; padding: 20px 80px; width: 60%; text-align: center; margin: 0 auto;}}
			#day-log {{grid-column: 1 / span 2; padding: 20px; margin: 0 auto; column-width: 20px;}}
			#today {{border: solid 1px black; padding:20px 60px; width: 40%; text-align: center; margin: 0 auto;}}
			#today-text {{line-height: 40px;}}	
			#grid-container {{display: grid; justify-content: space-evenly; grid-gap: 20px; grid-template-columns: 40% 60%; grid-template-rows: 30% 70%}}
			th, td {{padding: 10px; text-align: center; border-bottom: 1px dotted black}}
			th {{cursor: pointer;}}
		</style>
	</head>
	<body>
		<h1 id="title">Efficient Scanning Report</h1>
	<div id="grid-container">
		{}
		<div>
		{}
		</div>
		<div id="day-log" style="display:table">		
			<table id="DayLogTable">
				<tr>
				<th onclick ="sortTable(0, 1)">Date</th>
				<th onclick ="sortTable(1, 0)">Hours</th>
				<th onclick ="sortTable(2, 0)">Documents</th>
				<th onclick ="sortTable(3, 0)">Pages</th>
				<th onclick ="sortTable(4, 0)">Pages per Document</th>
				<th onclick ="sortTable(5, 0)">Pages per Hour</th>
				</tr>
				{}
			</table></div></div></body><script>
function sortTable(n, m) {{

  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount, xLTy = 0;
  table = document.getElementById("DayLogTable");
  switching = true;

  //Set the sorting direction to ascending:
  dir = "asc"; 

  /*Make a loop that will continue until
  no switching has been done:*/

  while (switching) {{

    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {{
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {{
        if (compareArgs(x.innerHTML,y.innerHTML,m)) {{
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
	}}
      }} else if (dir == "desc") {{
        if (compareArgs(y.innerHTML,x.innerHTML,m)) {{
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }}
      }}
    }}
    if (shouldSwitch) {{
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    }} else {{
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {{
        dir = "desc";
        switching = true;
      }}
    }}
  }}
}}

function compareArgs(x,y,mod){{
  var xLTy = false;
  if (mod == 1){{
    xLTy = compareDates(x,y);
  }} else {{
    xLTy = (Number(x) > Number(y));
  }}
  return xLTy;
}}

function compareDates(x,y){{
  date1 = x.split(" ");
  date1_v = Number(date1[1]) + calculateMonth(date1[2]) + + (Number(date1[3])*365)
  date2 = y.split(" ");
  date2_v = Number(date2[1]) + calculateMonth(date2[2])  + (Number(date2[3])*365)
  console.log(date1_v)
  return (date1_v > date2_v)
}}

function calculateMonth(month){{
  switch(month){{
    case "Jan": return 1 * 31;
    case "Feb": return 2 * 31;
    case "Mar": return 3 * 31; 
    case "Apr": return 4 * 31;
    case "May": return 5 * 31;
    case "Jun": return 6 * 31;
    case "Jul": return 7 * 31;
    case "Aug": return 8 * 31;
    case "Sep": return 9 * 31;
    case "Oct": return 10 * 31;
    case "Nov": return 11 * 31;
    case "Dec": return 12 * 31;
  }}
}}

</script>
</html>""".format(today_stats, overall_stats, day_log)
 