
import numpy as np

def twoPtForwardDiff(x,y):
    """Takes as arguments arrays of values x and y(x) and
    returns the derivates of y with respect to x using the
    forward difference method
    
    This method works by finding the slope of the curve y(x)
    measured over a small interval in the forward direction
    from x"""
    
    dydx = np.zeros(y.shape,float)

    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1]-x[-2])

    return dydx

def twoPtCenteredDiff(x,y):
    """Takes as arguments arrays of values x and y(x) and
    returns the derivates of y with respect to x using the
    center difference method
    
    This method works by finding the slope of the curve y(x)
    measured at the center of a small interval of x"""

    dydx = np.zeros(y.shape,float)

    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx

def fourPtCenteredDiff(x,y):
    """Takes as arguments arrays of values x and y(x) and
    returns the derivates of y with respect to x using the
    four-point center difference method
    
    This method works by finding the slope at the center of
    a small interval of x using 4 different points"""
    
    dydx = np.zeros(y.shape,float)
    
    h = x[1] - x[0] ## Assuming spacing of points in x is constant
    i = 2
    
    for z in np.nditer(dydx[2:-2], op_flags=['readwrite']):
        z[...] = ( y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2] ) / (12*h)
        i += 1
    
    dydx[0]  = (y[1] - y[0])/(x[1] - x[0])
    dydx[1]  = (y[2] - y[0])/(x[2] - x[0])
    dydx[-2] = (y[-3] - y[-1])/(x[-3] - x[-1])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx