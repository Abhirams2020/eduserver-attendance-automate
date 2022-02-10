
## this code is written and managed by abhinav -p (@_ai_factory) 
## abhinavhariharan2001@gmail.com

days=["monday","tuesday","wednesday","thursday","friday"]

#active classes are those classes for which you have to put attendance
#only those classes in the timetable which are in the active classes are considered by the
#automation script

#classes not in active classes are ignored by the script

active_classes=["gis","tfm","for"]


#timetable data with timetable format [[hour,minute],"subject_name"]
#order of slots doesn't matter .
#give the time of slot as the time when the link for attendance comes in the eduserver 
#for that specific course

timetable=[
	["monday",     [[8,0],"free"]	,   [[8,56],"free"] ,  	[[10,0],"gis"]		,	[[11,15],"free"]	,	[[12,55],"for"]	,	[[14,0],"tfm"] ],

	["tuesday",    [[8,0],"free"]  	,   [[8,55],"for"] 	,	[[10,15],"tfm"]   	,	[[11,15],"free"]	,	[[13,0],"free"]	,	[[14,0],"free"] ],

	["wednesday",  [[8,0],"free"]  	,   [[9,0],"free"]	, 	[[10,11],"free"]   	,	[[11,0],"gis"]		,  	[[13,0],"free"]	,  	[[13,55],"for"] ],

	["thursday",   [[7,45],"gis"] 	,   [[9,0],"free"]	, 	[[10,10],"for"] 	,	[[11,15],"tfm"]		, 	[[13,0],"free"]	, 	[[13,56],"free"] ],

	["friday",     [[8,00],"tfm"]  	,   [[9,0],"free"] 	, 	[[10,15],"free"] 	,	[[11,11],"free"]	,	[[13,10],"for"]	, 	[[14,0],"free"] ]

]

#provide the url for the course attandace page.. 
#its the address that we obtain from the address bar when we open the attendance section in
#eduserver for a course

# format ===> https://eduserver.nitc.ac.in/mod/attendance/view.php?id=$$$$$

course_web_url={
	
	"gis": "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=91038",

	"tfm": "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=90661",

	"for" : "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=90756"
}

class_url={
	
	"gis": "https://eduserver.nitc.ac.in/mod/webexactivity/view.php?id=91037&action=joinmeeting",

	"tfm": "https://eduserver.nitc.ac.in/mod/webexactivity/view.php?id=90659&action=joinmeeting",

	"for" : "https://eduserver.nitc.ac.in/mod/webexactivity/view.php?id=90748&action=joinmeeting"
}