def F(x):
    from pylab import *
    return array([5 * x[0] ** 2 - x[1] ** 2, x[1] ** 2 - 0.25 * (sin(x[0]) + cos(x[1]))])
