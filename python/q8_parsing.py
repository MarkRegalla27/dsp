#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
data = '/users/markregalla/desktop/metis/dsp_my_work_as_of_9-1-15/python/football.csv'

  def read_data(data):
    with open(data, 'rb') as f:
      reader = csv.reader(f)
      datalist = list(reader)
      return datalist
  
  datalist = read_data(data)

  def get_min_score_difference(datalist):
    i = 1
      difflist = []
      while i < len(datalist):
        sublist = datalist[i]
        difflist.append(abs(int(sublist[6]) - int(sublist[5])))
        i += 1
      return difflist,  min(difflist)
  
  difflist, minDiff = get_min_score(datalist)
  print 'The minimum difference between Goals and Goals Allowed is ' + str(minDiff)
  
  def get_team(difflist):
    i = 0
        k = 1
        while i < len(difflist) - 1:
                if difflist[i] > difflist[i + 1]:
                        k += 1
                i += 1
        return k + 1

  indexOfTeam = get_team(difflist)
  teamList = []
  teamList = datalist[indexOfTeam]
  team = teamList[0]
  print 'The team with the lowest difference is ' + team
