from numpy import sqrt
import matplotlib as pl
'''
@author: Arleigh Dickerson
@see: p17 and 18 of Sauer's Numerical Analysis, example 0.6
'''

# square root of the result of b squared minus the quantity of 4 times a times c
def sqrtTerm(a, b, c): return sqrt((b ** 2) - (4 * a * c))

# call to get x1 for a, b, c
def naiveX1(a, b, c): return (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)

# call to get x2 for a, b, c
# copy and paste with - instead of +...
def naiveX2(a, b, c): return (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

# second root (- part of eq) can be problematic if b is large compared to a or c
def naiveQuadratic(a, b, c):
    # a tuple with both root values. Values will be identical if double root.
    return (naiveX1(), naiveX2())

# use if b and sqrt(bsquared minus 4ac) are nearly equal in magniture
# and b is positive
def impl0dot13(a, b, c):
    def x1(): return -(b + sqrtTerm(a, b, c)) / (2 * a)
    def x2(): return -((2 * c) / (b + sqrtTerm(a, b, c)))
    return (x1(), x2())

# use if b and sqrt(bsquared minus 4ac) are nearly equal in magniture
# and b is negative
def impl0dot14(a, b, c):
    def x1(): return naiveX1(a, b, c)
    def x2(): return ((2 * c) / (-b + sqrtTerm(a, b, c)))
    return (x1(), x2())

def nearlyEqual(term0, term1) :
    threshold = 0.001  # arbitrary (for now)
    difference = abs(term0 - term1)
    return difference < threshold
