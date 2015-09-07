import csv
data = '/users/markregalla/desktop/metis/dsp_my_work_as_of_9-1-15/python/faculty.csv'

with open(data, 'rb') as f:
        reader = csv.reader(f)
        datalist = list(reader)

print datalist[0]

#Format for list order: name, degree, title, email
i = 1
emaillist = []
while i < len(datalist):
        sublist = datalist[i]
        emaillist.append(sublist[3])
        i += 1
print emaillist

thefile = open('/users/markregalla/desktop/metis/prework/faculty_email_list.csv', 'w')
for i in emaillist:
        thefile.write(i + ' \n')
thefile.close()
