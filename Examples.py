import numpy as np
import pylab as pl

def examplePlot():
    def randoms(): 
        return np.random.random(100)

    x = randoms()
    y = randoms()
    pl.plot(x, y, "ro")

    pl.show()
    return
