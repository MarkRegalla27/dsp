[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
import chap01soln
import thinkstats2
import nsfg
import nsfg2
import thinkplot
import random
import cumulative

i = 0
randset = []
for i in range(0,1000):
    randset.append(random.random())

pmf = thinkstats2.Pmf(randset, label='Random Nos. PMF')
thinkplot.Pmfs([pmf])
thinkplot.Show(xlabel='Number', ylabel='PMF')

cdf = thinkstats2.Cdf(randset, label='Random Nos. CDF')
thinkplot.Pmfs([cdf])
thinkplot.Show(xlabel='Number', ylabel='CDF')
'''

Above code works.  I cannot seem to figure out how to get the images it produces on 
Github
