import csv
import re
data = '/users/markregalla/desktop/metis/dsp_my_work_as_of_9-1-15/python/faculty.csv'

with open(data, 'rb') as f:
        reader = csv.reader(f)
        datalist = list(reader)
        
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

#Q1: Find number of different degrees:
        
#Q2: Find number of different titles:
        
#Q3: Print list of email addresses:
print emaillist

#Q4:
