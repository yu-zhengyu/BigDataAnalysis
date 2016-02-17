#!/usr/bin/env python

from operator import itemgetter
import sys

current_title = None
current_count = 0
date = None
title = None
thresdview = 100000 # the threshold
# init the 31 integer array, store 31 days review
datearray = [0 for x in range(0, 31)]

for line in sys.stdin:
	line = line.strip()
	# split the line into title and count : date
	title, countplusdate = line.split('\t')
	# split the second part into count and date
	count, date = countplusdate.split(':')
	# get the specific day
	dateindex = int(date[-2 : ]) - 1

	# if the title is same, add the count of view into specific array
	if current_title == title:
		datearray[dateindex] += int(count)
	else:
		if current_title:
			if sum(datearray) > thresdview:
			# contruct the printed information
				printinfo = str(sum(datearray)) + "\t"
				printinfo = printinfo + current_title
				dayhead = ""
				# print the all data each date
				for day in range(0, 31):
					if ((day + 1) / 10) == 0:
						dayhead = "2015120" + str(day + 1) + ":" + str(datearray[day])
					else:
						dayhead = "201512" + str(day + 1) + ":" + str(datearray[day])
					printinfo = printinfo + "\t" + dayhead
				print printinfo

		current_title = title
		datearray = [0 for x in datearray]
		datearray[dateindex] += int(count)

# print again, avoid miss last case
if current_title == title:
	if sum(datearray) > thresdview:
		printinfo = str(sum(datearray)) + "\t"
		printinfo = printinfo + current_title
		dayhead = ""
		for day in range(0, 31):
			if ((day + 1) / 10) == 0:
				dayhead = "2015120" + str(day + 1) + ":" + str(datearray[day])
			else:
				dayhead = "201512" + str(day + 1) + ":" + str(datearray[day])
			printinfo = printinfo + "\t" + dayhead
		print printinfo
