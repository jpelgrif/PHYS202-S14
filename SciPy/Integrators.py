
import numpy as np

def trapz(func,x,N):
    """
    Calculates and returns the integral of a function using
    the trapezoidal rule.
    
    Takes as arguments:
    the function, 
    the limits of integration as a tuple of floats (a,b),
    and the number of steps, N, used to calculate the integral
    """
    a,b = x
    h = (b-a)/N
    
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I

def simps(func,x,N):
    """
    Calculates and returns the integral of a function using
    Simpson's rule.
    
    Takes as arguments:
    the function, 
    the limits of integration as a tuple of floats (a,b),
    and the number of steps, N, used to calculate the integral
    """
    a,b = x
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    return (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum()\
                   + 2.*func(a+2*k2*h).sum())