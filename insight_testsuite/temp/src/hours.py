from datetime import datetime
from collections import defaultdict
import sys
import operator
import re

busyTimes = defaultdict(int)


print "Finding top 10 busiest in 60 min window..."
file = open(sys.argv[1],'r')
log_data = file.readlines()

start_time_tmp = log_data[0]
start_time_info = re.findall(r"\[(.*?)\]", start_time_tmp)

# Timestamp1 will be the time from the first line in the file
start_time = str(start_time_info[0]).split(" ")

for entry in log_data:

    time = re.findall(r"\[(.*?)\]", entry) # Regex to find the time from the line

    current_time = str(time[0]).split(" ") # gets the timestamp value

    t1 = datetime.strptime(start_time[0], "%d/%b/%Y:%H:%M:%S")
    t2 = datetime.strptime(current_time[0], "%d/%b/%Y:%H:%M:%S")
    difference = t2 - t1
    mins = difference.total_seconds()/60

    # creating dictionary for busyTimes and will increament the counter if
    # it is accessed again. Else the start_time will be changed to the current_time(current line time)
    # and the same logic will be applied for a different window of 60 mins
    if mins<60:

        if not start_time[0] in busyTimes:
            busyTimes[start_time[0]] = 1
        else:
            busyTimes[start_time[0]] += 1

    else:
        start_time[0] = current_time[0]
        if not start_time[0] in busyTimes:
            busyTimes[start_time[0]] = 1
        else:
            busyTimes[start_time[0]] += 1

sorted_busyTimes = sorted(busyTimes.items(), key=operator.itemgetter(1), reverse = True)[:10]

f = open(sys.argv[2], 'w')
for item in sorted_busyTimes:
    it = str(item).replace('\'','')
    p = re.search('\((.*?)\)', it)
    itemToReturn = p.group(1).replace(" ","")
    print>>f, itemToReturn
    # print>>f, itemToReturn

f.close()
