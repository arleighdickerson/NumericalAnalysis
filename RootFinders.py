'''
@author: Professor
'''
# import RootFinders as R

from numpy import ceil, log2
from math import fabs

# -------------------------------------------

def bisection(f,a,b,tol=1e-9):
	fa, fb = f(a), f(b)
	N = int( ceil( log2((b-a)/tol ) ) )
	
	x = []  # empty list
	
	for i in range(N):
		c = (b+a)/2
		x.append(c)
		fc = f(c)
		if fa*fc < 0:  # x* is in [a,c]
			b, fb = c, fc
		else:
			a, fa = c, fc
			
	x.append((b+a)/2)
	return x
	
# ----------------------------------------------

def newton(f,fp,x0,tol=1e-10,maxIt=50):
	dx, fx = 100, 100
	iter = 0
	xa = []
	xa.append(x0)
	x = x0
	
	while fabs(dx)>tol or fabs(fx)>tol and iter<=maxIt:
		fx, fpx = f(x), fp(x)
		dx = -fx/fpx
		print(dx)
		x += dx
		iter += 1
		xa.append(x)
		
	return xa
	
# ----------------------------------------------

from pylab import *

def newtonSystem(f,J,x0,tol=1e-10,maxIt=50):
	
	N = len(x0)
	dx, fx = ones((N,)), ones((N,))
	iter = 0
	xa = []
	xa.append(x0)
	x = x0
	
	while norm(dx,inf)>tol or norm(fx,inf)>tol and iter<=maxIt:
		fx, fpx = f(x), J(x)
#		dx = -fx/fpx
		dx = solve(fpx,-fx)
		x += dx
		iter += 1
		xa.append(x)
		
	return xa
