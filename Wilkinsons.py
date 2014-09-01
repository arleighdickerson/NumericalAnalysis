import numpy as np
from matplotlib import pyplot
from PIL.ImageChops import difference

N = 20

roots = range(1, N + 1)

inputValues = np.linspace(0, N, 600)

def clenshaw(x, index=1, accum=1):
    if index > N :
        return accum
    else :
        return clenshaw(x, index + 1, accum * (x - index))
    
# construct our (wilkinson's) polynomial instance
# verified output on wikipedia
def buildPolynomial():
    polynomialValue = np.poly1d([1])
    for i in range(1, N + 1) :
        polynomialValue *= np.poly1d([1, (i / -1)])
    return polynomialValue

#list of coefficients for our polynomial 
def coefficientList(ascendingDegrees = True):
    coefficients = buildPolynomial().coeffs.tolist()
    if(ascendingDegrees):
        coefficients.reverse()
    return coefficients

# param x, value to be evald
# param a, list of polynomial coeffs. DEGREES ARE ASCENDING
# verified output with mathematica
def naive(x, a=coefficientList()):
    accum = 0
    for k in range(len(a)):
        accum += a[k] * (x ** k)
    return accum

def testRoots(f):
    for x in range(1, N + 1):
        assert f(x) == 0

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
    coefficients = coefficientList()
    results = {}
    for x in inputValues:
        results[x] = naive(x, coefficients)
    return results

def showPlot(data):
    pyplot.semilogy(data.keys(), data.values(), "ro")
    pyplot.show()

def clenshawNaiveSemilog():
    clenshawData = makeClenshawData()
    naiveData = makeNaiveData()
    pyplot.semilogy(
                    clenshawData.keys(), clenshawData.values(), "ro",
                    naiveData.keys(), naiveData.values(), "bo")
    pyplot.show()
    
def plotDifferenceInAbs():
    clenshawData = makeClenshawData()
    naiveData = makeNaiveData()
    results = {}
    for x in inputValues:
        difference = clenshawData[x] - naiveData[x]
        results[x] = abs(difference)
    pyplot.semilogy(results.keys(), results.values(), "bo")
    
