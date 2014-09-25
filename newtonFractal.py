from pylab import *

ITERATIONS, DENSITY = 20, 1000
x_min, x_max, y_min, y_max = -1, 1, -1, 1
x, y = meshgrid(linspace(x_min, x_max, DENSITY), linspace(y_min, y_max, DENSITY))
z = x + 1j * y
for n in range(ITERATIONS):
    print('iteration {:d}'.format(n))
    z = 2 * (z ** 3) / (3 * z ** 2 - 1)

contourf(x, y, z, [-1, 0, 1], cmap=cm.summer)
colorbar()
show()