'''
Created on Sep 17, 2014

@author: Arleigh Dickerson
'''
from pylab import *

SEQUENCE_NUMBERS = range(1, 4)  # valid sequence numbers

'''
retrieves the ks for an error sequence
@precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
@param seqNum: the error sequence number for which to retrieve ks
@return: the ks for the error sequence specified by seqNum
'''
def keys(seqNum):
    assert seqNum in SEQUENCE_NUMBERS  # make sure sequence number is valid
    numberOfValues = len(values(seqNum))  # how many values are in sequence
    kMin = 100 if seqNum == 1 else 0  # specified in homework pdf
    kMax = numberOfValues + kMin  # maximum is dependent upon total number of values
    ks = range(kMin, kMax)  # all k values
    assert len(ks) == numberOfValues  # make sure we have the correct number of k values
    return ks  # all k values

'''
retrieves the values (evaluated ks) for an error sequence
@precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
@param seqNum: the error sequence number for which to retrieve values 
@return: the evaluated ks for the error sequence specified by seqNum
'''
def values(seqNum):
    assert seqNum in SEQUENCE_NUMBERS  # make sure sequence number is valid
    try:
        f = open("errorSequence" + str(seqNum) + ".txt", 'r')  # open the file in read-only mode
        lines = f.readlines()  # read the file line by line into a list of strings
        return map(float, lines)  # convert the list of strings into a list of floats
    finally:
        f.close()  # no matter what happens, close the file when we are done
    
'''
configures a geometric convergence plot for list of keys and values.
client code must call show() to make the plot visible.
@precondition: k and v are of equal length
@param k: the ks (keys) to plot
@param v: the evaluated ks (values) to plot
'''
def geometric(k, v):
    rho = (log10(v[-1]) 
       - log10(v[-2])) / (log10(v[-2]) 
                                - log10(v[-3]))  #FIX ME!!!
    print('rho = {:1.3f}'.format(rho))
    loglog(v[0:-2], v[1:-1])
    ylabel('$\log(|a_{k+1}|)$')
    xlabel('$\log(|a_k|)$')
    
'''
configures a linear geometric convergence plot for list of keys and values.
client code must call show() to make the plot visible.
@precondition: k and v are of equal length
@param k: the ks (keys) to plot
@param v: the evaluated ks (values) to plot
'''
def linearGeometric(k, v):
    S = 10 ** (log10(v[-1]) - log10(v[-2]))  #FIX ME!!!!!
    print('the asymptotic error constant is {:1.8f}'.format(S))
    semilogy(k, v, 'b')
    ylabel('$\log(|a_k|)$')
    xlabel('k')
    
'''
configures an algebraic convergence plot for list of keys and values.
client code must call show() to make the plot visible.
@precondition: k and v are of equal length
@param k: the ks (keys) to plot
@param v: the evaluated ks (values) to plot
'''
def algebraic(k, v):
    rho = (log10(v[-1]) 
           - log10(v[-2])) / (log10(k[-1]) 
                              - log10(k[-2]))
    print('rho = {:1.3f}'.format(-rho))
    loglog(k, v, 'k')
    ylabel('$\log(|a_k|)$')
    xlabel(r'$log(k)$')

'''
Used to show a plot, f,  of a sequence specified by seqNum.
Information about the sequence number and plot type will be printed to stdout.
@precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
@param f: a function that configures the plot to be shown. The function must 
    accept two arguments denoting the keys and values (respectively) to plot.
@param seqNum: the number of the sequence to plot
'''
def showPlot(f, seqNum):
    k = keys(seqNum)
    v = values(seqNum)
    print('sequence number: ' + str(seqNum))
    print('plot type: ' + str(f))
    f(k, v)
    show()
    print('')
    
'''
Shows all available plots for all sequences. 
Information about each plot will be printed to stdout.
'''
def showAll():
    for num in SEQUENCE_NUMBERS:
        for f in [plot, geometric, linearGeometric, algebraic]:
            showPlot(f, num)
