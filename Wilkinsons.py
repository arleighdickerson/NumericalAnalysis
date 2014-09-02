'''
@author: Arleigh Dickerson
'''

import numpy as np
from matplotlib import pyplot
i = 1
N = 20

domainMin = 0
domainMax = N
domainSize = 600

def roots() : 
    '''
    @return a list of roots for the Wilkinson's polynomial described by i and N.
    '''
    return range(i, N + 1)

def domain() : 
    '''
    @return a list containing the sampling domain described by domainMin, 
    domainMax, and domainSize.
    '''
    return np.linspace(domainMin, domainMax, domainSize)

def clenshaw(x, index=i, accum=1):
    '''
    @param x: the x-value for which the polynomial is to be evaluated.
    @param index: the index of the current iteration.  Clients call with default
        value.
    @param accum: the accumulator. Clients call with default value.
    @return: the clenshaw evaluation at x for a wilkinson's polynomial 
        parameterized by i and N
    '''
    if index > N:
        return accum
    else:
        return clenshaw(x, index + 1, accum * (x - index))
    
def wilkinson():
    '''
    @return a poly1d instance representing the Wilkinson's polynomial described 
        by i and N.
    '''
    return reduce(lambda b0, b1: b0 * b1,
                  map(lambda n:np.poly1d([1, abs(n) * -1]), roots()))

def coefficients(ascending=True):
    '''
    @param ascending: 
        True if the returned list should be sorted with degrees ascending, 
        False if the returned list should be sorted with degrees descending.
    @type ascending: bool
    @return a list of coefficients for the Wilkinson's polynomial described by
        i and N.
    '''
    coefficients = wilkinson().coeffs.tolist()
    if(ascending):
        coefficients.reverse()
    return coefficients

def naive(x, a=coefficients()):
    '''
    @param x: the x-value for which the polynomial is to be evaluated.
    @param a: a list of polynomial coefficients ordered by degree ASCENDING. 
        Defaults to the coefficients described by the Wilkinson's polynomial
        parameterized by i and N.
    @return: the naive evaluation at x for a polynomial with coefficients 
        described by a
    '''
    accum = 0
    for k in range(len(a)):
        accum += a[k] * (x ** k)
    return accum

def plotFunction(f):
    '''
    @param f: the function to plot
    '''
    d = domain()
    pyplot.semilogy(d, map(f, d), "ro")
    pyplot.show()
    
def plotDifference(f, g):
    '''
    @param f: a function for comparison
    @param g: a function for comparison
    '''
    d = domain()
    pyplot.semilogy(d, map(lambda x: abs(f(x) - g(x)), d), "ro")
    pyplot.show()
