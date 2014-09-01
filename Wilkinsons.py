import numpy as np
from matplotlib import pyplot

i = 1
N = 20

domainMin = 0
domainMax = N
domainSize = 600

def roots() : return range(i, N + 1)

def domain() : return np.linspace(domainMin, domainMax, domainSize)

def clenshaw(x, index=i, accum=1):
    if index > N :
        return accum
    else :
        return clenshaw(x, index + 1, accum * (x - index))
    
def wilkinson():
    return reduce(lambda b0,b1: b0 * b1, map(lambda n:np.poly1d([1, abs(n) * -1]), roots()))

def coefficients(ascendingDegrees=True):
    coefficients = wilkinson().coeffs.tolist()
    if(ascendingDegrees):
        coefficients.reverse()
    return coefficients

def naive(x, a=coefficients()):
    accum = 0
    for k in range(len(a)):
        accum += a[k] * (x ** k)
    return accum

def plotFunction(f):
    d = domain()
    pyplot.semilogy(d,map(f, d),"ro")
    pyplot.show()
    
def plotDifference(f,g):
    d = domain()
    pyplot.semilogy(d,map(lambda x: abs(f(x)-g(x)), d),"ro")
    pyplot.show()
    return
