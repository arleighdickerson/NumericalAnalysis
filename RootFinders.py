'''
@author: Arleigh Dickerson
'''
from numpy import ceil, log2, cos

def bisection(f, a, b, tol=1e9):
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

xStar = 0.86547403310161
a, b = 0, 2
def f(x): return cos(x) - x ** 3
print(bisection(f, a, b))
