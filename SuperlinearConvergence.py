'''
Created on Sep 11, 2014

@author: Arleigh Dickerson

@todo: fubar
'''

from pylab import *

N = 12
k = arange(1, N)
o = ones(N - 1)

quadratic = 1.0 / (2 ** (2 ** k))
geometric = exp(-k)

'''
print
m = 10 ** (log10(geometric[-1]) - log10(geometric[-2]))
print("the rate of geometric convergence is: {:1.4f}".format(m))
'''

loglog(
       geometric[0:-2],
       geometric[1:-1],
       'g',
       quadratic[0:-2],
       quadratic[1:-1],
       'b')
show()
