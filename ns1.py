from pylab import *
import RootFinders as R


def F(x):
    return array([5 * x[0] ** 2 - x[1] ** 2, x[1] ** 2 - 0.25 * (sin(x[0]) + cos(x[1]))])

def J(x):
    return array([
                  (10 * x[0]),
                  (-2 * x[1]),
                  (-0.25 * cos(x[0])),
                  (2 * x[1] + 0.25 * sin(x[1]))
                  ])
x0 = array([1.0, -1.0])
x = R.newtonSystem(F, J, x0)
