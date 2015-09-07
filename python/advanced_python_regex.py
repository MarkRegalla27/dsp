import csv
import re
data = '/users/markregalla/desktop/metis/dsp_my_work_as_of_9-1-15/python/faculty.csv'

with open(data, 'rb') as f:
	reader = csv.reader(f)
	datalist = list(reader)

#print datalist

#Format for list order: name, degree, title, email
i = 1
namelist = []
deglist = []
titlelist = []
emaillist = []
while i < len(datalist):
	sublist = datalist[i]
	namelist.append(sublist[0])
	deglist.append(sublist[1])
	titlelist.append(sublist[2])
	emaillist.append(sublist[3])
	i += 1

#Q1: find number of unique degrees
newdeglist = []
searchObj = []
i = 0
while i < len(deglist):
	newdeglist.append(deglist[i].split())
	i += 1
subdeglist = []
for deg in newdeglist:
	for subdeg in deg:
		subdeglist.append(subdeg)
noPeriodList = []
for deg in subdeglist:
	noPeriodList.append(re.sub('[.]', '', deg))
setDegList = set(noPeriodList)
i = 0
count = 0
for l in setDegList:
	while i < len(noPeriodList):
		if l == noPeriodList[i]:
			count += 1
		i += 1
	print 'There are ' + str(count) + ' personnel with the degree "' + str(l) + '".'
	count = 0
	i = 0

#Q2: find how many different titles there are
i = 0
count = 0
setTitleList = set(titlelist)
print setTitleList
for l in setTitleList:
	while i < len(titlelist):
		if l == titlelist[i]:
			count += 1
		i += 1
	print 'There are ' + str(count) + ' personnel with the title "' + str(l) + '".'
	count = 0
	i = 0

#Q3: print email addresses
print emaillist

#Q4: find unique email domains
#print emaillist
domainList = []
i = 0
while i < len(emaillist):
	searchObj = re.search(r'@.*$', emaillist[i])
	domainList.append(searchObj.group())
	i += 1
setDomainList = set(domainList)
i = 0
count = 0
for l in setDomainList:
	while i < len(domainList):
		if l == domainList[i]:
			count += 1
		i += 1
	print 'There are ' + str(count) + ' personnel with the email domain "' + str(l) + '".'
	count = 0
	i = 0
