from math import cos, sin, pi, fabs

def f(x): return cos(x) - sin(x)
def g(x): return x + f(x) 

xStar = 0.25 * pi
x = 0
e = fabs(xStar - x)

for n in range(1, 17):
    xN = g(x)
    eN = fabs(xStar - x)
    print('{0:8d} {1:8f} {3:8f} {4:8f}'.format(n, xN, g(xN), eN, eN / e))
    x = xN
    e = eN
