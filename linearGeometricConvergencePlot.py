# cd C:\Users\Scott\Documents\books\na\chapters\intro
# run linearGeometricConvergencePlot.py (cPlot1.eps)

from pylab import *

N = 24
k = arange(1,N)

# sequences converging to zero at different rates
algebraic = 1.0/k**2
geometric = exp(-k)

print(' ')
S = 10**(log10(geometric[-1]) - log10(geometric[-2])) 
print('the asymptotic error constant is {:1.8f}'.format(S))


semilogy(k,algebraic,'b',k,geometric,'g')
legend(('algebraic','geometric'),'lower left') #,fontsize='medium')
ylabel('$\log(|a_k|)$')
xlabel('k')
show()