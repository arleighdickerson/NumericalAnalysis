'''
@author: Arleigh Dickerson
'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

XLIMS = (-1, 1)
YLIMS = (-1, 1)

ITERATIONS = 20
DENSITY = 1000

# grab the figure reference for later
fig = plt.figure()

x, y = np.meshgrid(
                   np.linspace(min(XLIMS), max(XLIMS), DENSITY),
                   np.linspace(min(YLIMS), max(YLIMS), DENSITY))

zs = [x + 1j * y]
for i in range(0, ITERATIONS):
    zs.append(2 * (zs[-1] ** 3) / (3 * zs[-1] ** 2 - 1))

def animate(frame):
    '''
     @param frame: the current frame number. Starts at zero.
     @type frame: int
    '''
    return plt.contourf(x, y, zs[frame - 1], [-1, 0, 1], cmap="summer")

# we need the anim reference to be in scope for the animation to proceed
# I have no idea why
anim = animation.FuncAnimation(fig, animate, interval=20, frames=ITERATIONS)

plt.show()
