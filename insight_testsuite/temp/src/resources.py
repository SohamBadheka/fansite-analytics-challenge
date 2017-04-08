from collections import defaultdict
import collections
import sys
import operator
import re
bandwidthResult = defaultdict(int)

print "Finding top 10 resources that consume the most bandwidth"
file = open(sys.argv[1], 'r')
log_data = file.readlines()
resources = []
bandwidthData = []

def bandwidth(requestData):
	bandwidthData = requestData.strip().split(" ") # This will have status code and byte information
	# Making sure that each bandwidth value should be valid by checking whether its an integer or not
	# This also includes '-' case and '2029c' case
	try:
		int(bandwidthData[1])
		return bandwidthData[1]
	except ValueError:
		return '0'

for entry in log_data:

	# Spliting the line by " " so that the first part will contain everything before
	# " " and the a[1] first index will contain the data within " " and the a[2] will have the
	# data after " "
	entry_data = entry.split("\"")

	# While Spliting the line with "" regex, if exact three partitions are created, then it is the
	# ideal case, how we want the data. But there can be some cases when the data is dirty and there are
	# quotes in between the quotes, so handling that by partition size


	if(len(entry_data) == 5):

		entry_data[2] = entry_data[4]


	if(len(entry_data) == 4):

		entry_data[2] = entry_data[3]


	entry_data[2].replace("\"","")

	# info will contain the data before "GET ..."

	responseInfo = entry_data[1].split(" ") #responseInfo should be splitted so that we can get the resource name etc.
	res = re.findall(r"/.*", entry_data[1]) # here we are only interested in request resource, which will contain '/' in it


	for data in res:

		first = data.split(" ") # Spliting bodies of resource and http/1.0 family if it is available.

		# There can be two fields which contain '/' in its body, so further checking that
		#it must contain '/' in start of its body
		pattern = "(/([\D+]).*)"

		regex = re.compile(pattern, re.IGNORECASE)

		# here we are only checking for the first index value after splitting
		# because it can either be a resource or an http family.
		for match in regex.finditer(first[0]):
			resources.append(first[0])
			# Making an array of bandwidthData which will have bandwidth information, just for valid resources.
			# Otherwise that bandwidth should not be counted.
			bandwidthData.append(bandwidth(entry_data[2]))


for index, item in enumerate(resources):
	# print item+" "+bandwidthData[index]+"\n"
	if not item in bandwidthResult:
		bandwidthResult[item] = int(bandwidthData[index])
   	else:
		bandwithSum = int(bandwidthResult[item]) + int(bandwidthData[index])
		bandwidthResult[item] = bandwithSum

sorted_bandwidthResult = sorted(bandwidthResult.items(), key=operator.itemgetter(1), reverse = True)[:10]


f = open(sys.argv[2], 'w')
for item in sorted_bandwidthResult:
	it = str(item).replace('\'','')
	p = re.search('\((.*?)\)', it)
	res = p.group(1).replace(" ","")
	itemToReturn = res.split(',')
  	print>>f, str(itemToReturn[0])

f.close()
