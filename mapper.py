#!/usr/bin/env python
import os, sys

# author: Yu Zheng
# Andrew ID: yuzheng
# Date: 1/27/2016

# set the useless page content
Useless_page = ["Media:", "Special:", "Talk:", "User:", "User_talk:", "Project:", "Project_talk:", "File:", "File_talk:", "MediaWiki:", "MediaWiki_talk:", "Template:", "Template_talk:", "Help:", "Help_talk:", "Category:", "Category_talk:", "Portal:", "Wikipedia:", "Wikipedia_talk:"]

# set the useless page content
Useless_ima_file = [".jpg", ".gif", ".png",".JPG", ".GIF", ".PNG", ".txt", ".ico"]

# set the useless page content
Userless_page_content = ["404_error/", "Main_Page", "Hypertext_Transfer_Protocol", "Search"]

# get the file name 
filename = os.environ["mapreduce_map_input_file"]
#filename = "s3://cmucc-datasets/wikipediatraf/201512/pagecounts-20151201-000000"

filenames = filename.split("-")
date = filenames[-2]

for oneline in sys.stdin:
	# split the line into 4 parts(or 3 parts)
	splitline = oneline.split()

	# skip if the length is less than 4, it is not start as en and the first char is not uppercase
	if len(splitline) == 4 and splitline[0] == "en" and not splitline[1][0].islower():

		# skip if the title contain useless content
		iscontinue = False
		for match in Useless_page:
			if splitline[1].startswith(match):
				iscontinue = True
				break

		if iscontinue:
			continue

		# skip if content is image or text
		for match in Useless_ima_file:
			if(splitline[1].endswith(match)):
				iscontinue = True
				break
		if iscontinue:
			continue

		# skip if title is useless page content
		if splitline[1] in Userless_page_content:
			continue
		# print the title	
		print '%s\t%s:%s' % (splitline[1], splitline[2], date)
