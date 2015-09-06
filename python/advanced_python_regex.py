import csv
import re
data = '/users/markregalla/desktop/metis/dsp_my_work_as_of_9-1-15/python/faculty.csv'

with open(data, 'rb') as f:
        reader = csv.reader(f)
        datalist = list(reader)
