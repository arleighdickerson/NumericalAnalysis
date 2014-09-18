'''
Created on Sep 17, 2014

@author: Arleigh Dickerson
'''
from pylab import log10, plot, loglog, semilogy, xlabel, ylabel, title, show

SEQUENCE_NUMBERS = range(1, 4)  # valid sequence numbers

def keys(seqNum):
    '''
    retrieves the ks for an error sequence
    @precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
    @param seqNum: the error sequence number for which to retrieve ks
    @return: the ks for the error sequence specified by seqNum
    '''
    assert seqNum in SEQUENCE_NUMBERS  # make sure sequence number is valid
    numberOfValues = len(values(seqNum))  # how many values are in sequence
    kMin = 100 if seqNum == 1 else 0  # specified in homework pdf
    kMax = numberOfValues + kMin  # maximum is dependent upon total number of values
    ks = range(kMin, kMax)  # all k values
    assert len(ks) == numberOfValues  # make sure we have the correct number of k values
    return ks  # all k values

def values(seqNum):
    '''
    retrieves the values (evaluated ks) for an error sequence
    @precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
    @param seqNum: the error sequence number for which to retrieve values 
    @return: the evaluated ks for the error sequence specified by seqNum
    '''
    assert seqNum in SEQUENCE_NUMBERS  # make sure sequence number is valid
    try:
        f = open("errorSequence" + str(seqNum) + ".txt", 'r')  # open the file in read-only mode
        lines = f.readlines()  # read the file line by line into a list of strings
        return map(float, lines)  # convert the list of strings into a list of floats
    finally:
        f.close()  # no matter what happens, close the file when we are done
    
def showPlot(f, seqNum):
    '''
    Used to show a plot, f,  of a sequence specified by seqNum.
    Information about the sequence number and plot type will be printed to stdout.
    @precondition: seqNum is a member of SEQUENCE_NUMBERS 
    and the appropriate file exists in the current working directory.
    @param f: a function that configures the plot to be shown. The function must 
    accept two arguments denoting the keys and values (respectively) to plot.
    @param seqNum: the number of the sequence to plot
    '''
    k = keys(seqNum)
    v = values(seqNum)
    print('sequence: ' + str(seqNum))
    print('plot type: ' + f.__name__)
    f(k, v)
    title("type:" + f.__name__ + ", sequence:" + str(seqNum))
    # savefig(f.__name__ + str(seqNum) + '.png', bbox_inches='tight')
    show()
    print('')

def geometric(k, v):
    '''
    configures a geometric convergence plot for list of keys and values.
    client code must call show() to make the plot visible.
    @precondition: k and v are of equal length
    @param k: the ks (keys) to plot
    @param v: the evaluated ks (values) to plot
    '''
    rho = (log10(v[-1]) 
       - log10(v[-2])) / (log10(v[-2]) 
                                - log10(v[-3]))  
    print('rho = {:1.3f}'.format(rho))
    loglog(v[0:-2], v[1:-1])
    ylabel('$\log(|a_{k+1}|)$')
    xlabel('$\log(|a_k|)$')
    
def linearGeometric(k, v):
    '''
    configures a linear geometric convergence plot for list of keys and values.
    client code must call show() to make the plot visible.
    @precondition: k and v are of equal length
    @param k: the ks (keys) to plot
    @param v: the evaluated ks (values) to plot
    '''
    S = 10 ** (log10(v[-1]) - log10(v[-2]))  #FIX ME!!!!!
    print('the asymptotic error constant is {:1.8f}'.format(S))
    semilogy(k, v, 'b')
    ylabel('$\log(|a_k|)$')
    xlabel('k')
    
def algebraic(k, v):
    '''
    configures an algebraic convergence plot for list of keys and values.
    client code must call show() to make the plot visible.
    @precondition: k and v are of equal length
    @param k: the ks (keys) to plot
    @param v: the evaluated ks (values) to plot
    '''
    rho = (log10(v[-1]) 
           - log10(v[-2])) / (log10(k[-1]) 
                              - log10(k[-2]))
    print('rho = {:1.3f}'.format(-rho))
    loglog(k, v, 'k')
    ylabel('$\log(|a_k|)$')
    xlabel(r'$log(k)$')

    
def showAll():
    '''
    Shows all available plots for all sequences. 
    Information about each plot will be printed to stdout.
    '''
    for num in SEQUENCE_NUMBERS:
        for f in [plot, geometric, linearGeometric, algebraic]:
            showPlot(f, num)
