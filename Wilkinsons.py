import numpy as np

N = 20

inputValues = np.linspace(0, N, 600)

def clenshaw(x, index=1, accum=1):
    if index > N :
        return accum
    else :
        return clenshaw(x, index + 1, accum * (x - index))
    
#ensures that roots evaluate to zero (low hanging fruit)
def clenshawTest() :
    for x in range(1,N+1):
        assert clenshaw(x) == 0

#construct our (wilkinson's) polynomial instance
#verified output on wikipedia
def buildPolynomial():
    polynomialValue = np.poly1d([1])
    for i in range(1,N+1) :
        polynomialValue *= np.poly1d([1,(i / -1)])
    return polynomialValue

#param x, value to be evald
#param a, list of polynomial coeffs. DEGREES ARE ASCENDING
#verified output with mathematica
def naive(x,a):
    accum = 0
    for k in range(len(a)):
        accum += a[k] * (x ** k)
    return accum

def makeClenshawData():
    results = {}
    for x in inputValues:
        results[x] = clenshaw(x)
    return results


def makeNumpyPolyData():
    polynomial = buildPolynomial()
    results = {}
    for x in inputValues:
        results[x] = polynomial(x)
    return results

def makeNaiveData():
    coefficients = buildPolynomial().coeffs.tolist()
    coefficients.reverse()
    results = {}
    for x in inputValues:
        results[x] = naive(x, coefficients)
    return results