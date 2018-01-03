# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:18:12 2017
@author: JFord
"""
import numpy as np
import math
import scipy.optimize as opt
import pylab


def model(t, Ti, Ta, c):
    """
    Models the cooling of a cup of coffee taking as an input:
    t is the time in seconds
    Ti is the initial temperature of the tea
    Ta is the ambient temperature the temperature will eventually reach
    c is the time constant for the cooling process
    Returns the result of the model equation
    """
    return (Ti - Ta) * (math.e ** (-t / c)) + Ta


def read2coldata(filename):
    """
    Reads from an input file with two coloumns sepereated by whitespace
    and returns a tuple of two numpy arrays, with the first array being
    the values of the first column and vice versa.
    """
    f = open(filename, 'r')
    vals = f.readlines()
    f.close()
    x = []
    y = []
    for lines in vals:
        lline = list(lines.split())
        print(lline)
        x.append(float(lline[0]))
        y.append(float(lline[-1]))
    xnp = np.array(x)
    ynp = np.array(y)
    tup = (xnp, ynp)
    return tup


def extract_parameters(ts, Ts):
    """
    Expects a numpy array as an input for ts
    and Ts where ts is the time values and Ts is
    the time values. The function esitmates and
    returns a tuple of the three model parameters
    Ti, Ta, and c by fitting the model function to
    the data ts and Ts
    """
    p, pcov = opt.curve_fit(model, ts, Ts, p0=[100, 25, 10])
    a, b, c = p
    lst = [a, b, c]
    return lst


def sdt(Ti, Ta, c):
    return c * math.log


def sixty_degree_time(Ti, Ta, c):
    """
    Takes as an input Ti, Ta, and c and returns an estimate of the
    number of seconds required for the temperature of the drink to reach
    60 degrees celsius.
    """
    fsolve(sdt, x0)
# Below is a function for manually examining fit


def plot(ts, Ts, Ti, Ta, c):
    """Input Parameters:

      ts : Data for time (ts)
                (numpy array)
      Ts : data for temperature (Ts)
                (numpy arrays)
      Ti : model parameter Ti for Initial Temperature
                (number)
      Ta : model parameter Ta for Ambient Temperature
                (number)
      c  : model parameter c for the time constant
                (number)

    This function will create plot that shows the model fit together
    with the data.

    Function returns None.
    """
    Ti = extract_parameters(ts, Ts)[0]
    Ta = extract_parameters(ts, Ts)[1]
    c = extract_parameters(ts, Ts)[2]
    pylab.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    pylab.plot(ts, fTs, label='fitted')
    pylab.legend()
    pylab.show()
