from collections import defaultdict
import operator
import sys
import re
result = defaultdict(int)

print "Finding most active IP addresses..."
files = open(sys.argv[1], 'r')


log_data = files.readlines()
files.close()

for entry in log_data:
	entry_data = entry.split(" ")

	if not entry_data[0] in result:
        	result[entry_data[0]] = 1
    	else:
        	result[entry_data[0]] += 1

sorted_r = sorted(result.items(), key=operator.itemgetter(1), reverse = True)[:10]

# print sorted_r
f = open(sys.argv[2], 'w')
for item in sorted_r:
	it = str(item).replace('\'','')
	p = re.search('\((.*?)\)', it)
	itemToReturn = p.group(1).replace(" ","")
  	print>>f, itemToReturn

f.close()
