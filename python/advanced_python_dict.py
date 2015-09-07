#Q6: Create dictionary with last name as key and degree, title, email as values
faculty_dict = {}
rowList = []
lineList = []
i = 0
while i < len(datalist) - 1:
	lineList.append(deglist[i])
	lineList.append(titlelist[i])
	lineList.append(emaillist[i])
	rowList.append(lineList)
	lineList = []
	i += 1
lastnames = []
thenames = []
i = 0
while i < len(namelist) - 1:
	thenames = namelist[i].split()
	lastnames.append(thenames[-1:])
	i += 1
faculty_dict = zip(lastnames, rowList)
print faculty_dict[0:3]

#Q7: Add the full name to the keys in the dictionary from Q6
allNames = []
rowList = []
lineList = []
i = 0
while i < len(datalist) - 1:
	lineList.append(deglist[i])
	lineList.append(titlelist[i])
	lineList.append(emaillist[i])
	rowList.append(lineList)
	lineList = []
	i += 1
i = 0
while i < len(namelist) - 1:
	allNames.append(namelist[i].split())
	i += 1
professor_dict = zip(allNames, rowList)
print sorted(professor_dict[0:3])

#Q8: Print new dictionary sorted by last name
#The raw data file imported was sorted by first name at the get-go.
#Removing the sorted function from the printing of professor_dict will return
#the list sorted the same as the raw data file
print professor_dict[0:3]

