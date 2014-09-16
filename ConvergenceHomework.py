from numpy import log
from matplotlib import pyplot as pl

# 1 : Algebraic Convergence
# 2 : Geometric Convergence
# 3 : Superlinear Geometric Convergence
seqNum = 2

def readContent():
    try:
        f = open("errorSequence" + str(seqNum) + ".txt", 'r')
        lines = f.readlines()
        return map(float, lines)
    finally:
        f.close()

data = readContent()
kFloor = 100 if seqNum == 1 else 0
kCeiling = len(data) + kFloor
ks = range(kFloor, kCeiling)

def a(k):
    assert k in ks
    return data[k - kFloor]

def coefficients(rho=1):
    accum = []
    for k in ks[1:]:
        v0 = a(k - 1)
        v1 = a(k)
        accum.append(v1 / (v0 ** rho))
    return accum

def plotAlgebraic(rho, C):
    def lhs(k): return log(a(k))
    def rhs(k): return log(C) + (rho * log(k))
    pl.plot(map(lhs, ks), map(rhs, ks))

def plotSuperLinear(rho, S):
    d = ks[1:]
    def lhs(k): return log(a(k))
    def rhs(k): return log(S) + rho * log(a(k - 1))
    pl.plot(map(lhs, d), map(rhs, d))
    
def plotGeometric(S):
    logOfa0 = log(a(0))
    def lhs(k): return abs(log(a(k)))
    def rhs(k): return abs(k * log(S) + logOfa0)
    pl.plot(map(lhs, ks), map(rhs, ks))

def showPlot():
    if seqNum == 1:
        plotGeometric(coefficients()[-1])
    elif seqNum == 2:
        plotGeometric(coefficients()[-1])
    elif seqNum == 3:
        rho = 3
        plotSuperLinear(rho, coefficients(rho)[-1])
    pl.show()
