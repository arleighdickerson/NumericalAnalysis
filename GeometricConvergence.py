'''
Created on Sep 11, 2014

@author: Arleigh Dickerson
'''

from pylab import *

N = 24
k = arange(1, N)

algebraic = 1.0 / k ** 2
geometric = exp(-k)

print
m = 10 ** (log10(geometric[-1]) - log10(geometric[-2]))
print("the rate of geometric convergence is: {:1.4f}".format(m))

semilogy(k, algebraic, "b", k, geometric, "g")
show()
