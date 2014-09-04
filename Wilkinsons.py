import numpy as np
from matplotlib import pyplot
'''
@author: Arleigh Dickerson
'''

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
    @return: the clenshaw evaluation at x for a numpyPolynomial's polynomial 
        parameterized by i and N
    '''
    if index > N:
        return accum
    else:
        return clenshaw(x, index + 1, accum * (x - index))
    
def makePolynomial() :
    a = coefficients()
    a.reverse()
    return np.poly1d(a)
    
def coefficients():
    return [2432902008176640000,
            - 8752948036761600000,
            13803759753640704000,
            - 12870931245150988800,
            8037811822645051776,
            - 3599979517947607200,
            1206647803780373360,
            - 311333643161390640,
            63030812099294896,
            - 10142299865511450,
            1307535010540395,
            - 135585182899530,
            11310276995381,
            - 756111184500,
            40171771630,
            - 1672280820,
            53327946,
            - 1256850,
            20615,
            - 210,
            1]

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
