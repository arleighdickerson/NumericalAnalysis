'''
Created on Sep 17, 2014

@author: Arleigh Dickerson
'''
from pylab import *

def keys(seqNum):
    length = len(values(seqNum))  # inefficient
    assert seqNum in range(1, 4)
    kMin = 100 if seqNum == 1 else 0
    kMax = length + kMin
    ks = range(kMin, kMax)
    assert len(ks) == length
    return ks

def values(seqNum):
    assert seqNum in range(1, 4)
    try:
        f = open("errorSequence" + str(seqNum) + ".txt", 'r')
        lines = f.readlines()
        return map(float, lines)
    finally:
        f.close()

def convergenceType(rho):
    if rho == 1:
        return "geometric"
    elif rho == 2:
        return "quadratic"
    else:
        return "?"

def geometric(k, v):
    rho = (log10(v[-1]) 
       - log10(v[-2])) / (log10(v[-2]) 
                                - log10(v[-3]))
    print(convergenceType(rho) + ', rho = {:1.3f}'.format(rho))  # geometric or quadratic?
    loglog(v[0:-2], v[1:-1])
    ylabel('$\log(|a_{k+1}|)$')
    xlabel('$\log(|a_k|)$')
    
def linearGeometric(k, v):
    S = 10 ** (log10(v[-1]) - log10(v[-2]))
    print('the asymptotic error constant is {:1.8f}'.format(S))
    semilogy(k, v, 'b')
    ylabel('$\log(|a_k|)$')
    xlabel('k')
    
def algebraic(k, v):
    rho = (log10(v[-1]) 
           - log10(v[-2])) / (log10(k[-1]) 
                              - log10(k[-2]))
    print('rho = {:1.3f}'.format(-rho))
    loglog(k, v, 'k')
    ylabel('$\log(|a_k|)$')
    xlabel(r'$log(k)$')

def showPlot(f, seqNum):
    k = keys(seqNum)
    v = values(seqNum)
    print(k)
    print(v)
    f(k, v)
    show()

def showAll(seqNum):
    showPlot(geometric, seqNum)
    showPlot(linearGeometric, seqNum)
    showPlot(algebraic, seqNum)

map(showAll, range(1, 4))
# linearGeometric(k1, v1)
# linearGeometric(k2, v2)
