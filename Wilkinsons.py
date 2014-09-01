import numpy as np

N = 20

inputValues = np.linspace(0, N, 600)

def clenshaw(x, index=1, accum=1):
    if index > N :
        return accum
    else :
        return clenshaw(x, index + 1, accum * (x - index))
    
def clenshawTest() :
    for x in range(1,N+1):
        assert clenshaw(x) == 0

#construct our (wilkinson's) polynomial instance
def buildPolynomial():
    polynomialValue = np.poly1d([1])
    for i in range(1,N+1) :
        polynomialValue *= np.poly1d([1,(i / -1)])
    return polynomialValue
