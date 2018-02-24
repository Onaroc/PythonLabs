# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:08:38 2017
@author: JFord
"""

import math


def degree(x):
    """
    Takes an argument x in radian and returns the
    cooresponding value in degrees.
    """
    return x * (180 / math.pi)


def min_max(xs):
    """
    Computes the minimum value xmin in the list xs, and the maximum value
    xmax of the elements in the list, and returns a tuple (xmin,xmax).
    """
    xmin = min(xs)
    xmax = max(xs)
    return (xmin, xmax)


def geometric_mean(xs):
    """
    Returns the geometric mean of the numbers given in the list xs.
    """
    n = len(xs) - 1
    p = xs[n]
    while n > 0:
        n = n - 1
        p = p * xs[n]
    return p ** (1 / len(xs))


def swing_time(L):
    """
    Returns the time T [in seconds] needed for an idealized pendulum
    of length L [in meters] to complete a single oscillation.
    """
    return (2 * math.pi) * (L / 9.81) ** (1/2)


def range_sqaured(n):
    """
    Takes an non-negative integer value n and that
    returns the list [0, 1, 4, 9, 16, 25, ..., (n-1)^2].
    """
    lst = range(n)
    sqlst = [x ** 2 for x in lst]
    return sqlst


def count(element, seq):
    """
    Counts how often the given element 'element' occurs in the
    given sequence 'seq', and returns this as an integer value.
    """
    return seq.count(element)
