'''
@author: Arleigh Dickerson
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

XLIMS = (-1, 1)
YLIMS = (-1, 1)

ITERATIONS = 20
DENSITY = 1000

x, y = np.meshgrid(
                   np.linspace(min(XLIMS), max(XLIMS), DENSITY),
                   np.linspace(min(YLIMS), max(YLIMS), DENSITY))

def zGenerator():
    z = x + 1j * y
    for n in range(ITERATIONS):
        yield z
        print('iteration {:d}'.format(n + 1))
        z = 2 * (z ** 3) / (3 * z ** 2 - 1)

zs = zGenerator()

def animate(frame):
    '''
     @param frame: the current frame number. Starts at zero.
     @type frame: int
     @return: the stuff to be contained within frame of to be animated
    '''
    return plt.contourf(x, y, zs.next(), [-1, 0, 1], cmap="summer", blit=True)

# the figure to add animations to
fig = plt.figure()

# we need the anim reference to be in scope for the animation to proceed
# I have no idea why
anim = FuncAnimation(fig, animate, frames=ITERATIONS)

plt.show()
