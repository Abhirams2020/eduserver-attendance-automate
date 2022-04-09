# Eduserver-attendance-automate

A python script for attendance automation in the Eduserver for NITC.

By using python for web scraping, the program marks the attendance on Eduserver and also opens the corresponding class at the right time.

Users can input username and password in the auto.py file and modify the timetable.py file to use the program.

External libraries used
-----------------------
1: selenium

How to install selenium
-----------------------
pip install selenium

How to run script
-----------------
python auto.py

Important information regarding selenium
----------------------------------------
The code uses the chrome driver for automating the web browser . 
Make sure you have chrome installed and running on your pc.

Install a chrome driver from https://chromedriver.chromium.org/downloads

Whats inside
-------------
1. timetable.py

Contains data for timetable, attendance links and class meeting links

Timetable data with timetable format [[hour,minute],"subject_name"]

Order of slots doesn't matter .

Give the time of slot as the time when the link for attendance comes in the eduserver 

2. auto.py

Main script file

Provide user details here

You can change the working of the script from here

Important parameters in auto.py
------------------------------
1:login_username 

2:login_password

3:max_attempts : max number of retry 


About this script
-----------------
Forked from https://github.com/AI-Factor-y/Attendance-automation. It is still under development so proceed at your own risk.

Licensed under [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/AI-Factor-y/Attendance-automation/blob/main/LICENSE)

Any contribution to this code will be helpful. Please feel free to commit.
