# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_start_date = datetime.strptime(date_start, '%m-%d-%Y')     #m, d, Y in place for month, day, year
date_stop_date = datetime.strptime(date_stop, '%m-%d-%Y')       #be sure to have '-' between %m, %d, and %Y as the strings
diff = date_stop_date - date_start_date                         #above contain them
print diff
>>> 937 days, 0:00:00

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start_stamp = datetime.fromtimestamp(int(date_start))
date_stop_stamp = datetime.fromtimestamp(int(date_stop))
print date_stop_stamp - date_start_stamp
>>> -82 days, 14:13:22

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
 
date_start_script = datetime.strptime(date_start, '%d-%b-%Y')
date_stop_script = datetime.strptime(date_stop, '%d-%b-%Y')
print date_stop_script - date_start_script
>>> 7850 days, 0:00:00
