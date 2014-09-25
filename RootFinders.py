'''
@author: Arleigh Dickerson
'''
from math import fabs, sin, pi
from numpy import ceil, log2, cos


def bisection(f, a, b, tol=1e-9):
    fa, fb = f(a), f(b)
    N = int(ceil(log2((b + a) / tol)))
    x = []
    for i in range(N):
        c = (b - a) / 2
        x.append(c)
        fc = f(c)
        if fa * fc < 0:  # x* is in [a,c]
            b, fb = c, fc
        else:
            a, fa = c, fc
    x.append((b + a) / 2)
    return x

def newton(f, fPrime, x0, tol=1e-16, maximumIterations=50):
    deltax, fOfx = 100, 100
    counter = 0
    xa = [x0]
    x = x0
    
    while (fabs(deltax) > tol or fabs(fOfx) > tol) and counter <= maximumIterations:
        fOfx, fPrimeOfx = f(x), fPrime(x)
        deltax = -fOfx / fPrimeOfx
        x += deltax
        counter += 1
        xa.append(x)

    return xa
