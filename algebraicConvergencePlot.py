# cd C:\Users\Scott\Documents\books\na\chapters\intro
# run algebraicConvergencePlot.py (cPlot3.eps)

from pylab import *

N = 40
k = arange(1,N)

# sequences converging to zero at different rates
algebraic = 1.0/k**2
geometric = exp(-k)


print(' ')
rho = (log10(algebraic[-1]) - log10(algebraic[-2]))/(log10(k[-1]) - log10(k[-2]))
print('algebraic, rho = {:1.3f}'.format(-rho))

loglog(k,algebraic,'k',k,geometric)
legend(('algebraic','geometric'),'lower left' )
ylabel('$\log(|a_k|)$')
xlabel(r'$log(k)$')

show()