# cd C:\Users\Scott\Documents\books\na\chapters\intro
# run geometricConvergencePlot.py (cPlot2.eps)

from pylab import *

N = 26
k = arange(1,N)

N2 = 8
k2 = arange(1,N2)

geometric = exp(-k)
quadratic = 1.0/(2**(2*ones(N2-1))**k2)     # 2^(2^k)

print(' ')

rho = (log10(geometric[-1]) - log10(geometric[-2]))/(log10(geometric[-2]) - log10(geometric[-3]))
print('geometric, rho = {:1.3f}'.format(rho))

rho = (log10(quadratic[-1]) - log10(quadratic[-2]))/(log10(quadratic[-2]) - log10(quadratic[-3]))
print('quadratic, rho = {:1.3f}'.format(rho))

loglog(geometric[0:-2],geometric[1:-1], 'g',quadratic[0:-2],quadratic[1:-1], 'b' )
legend(('linear', 'quadratic'),'upper left' )

ylabel('$\log(|a_{k+1}|)$')
xlabel('$\log(|a_k|)$')

show()