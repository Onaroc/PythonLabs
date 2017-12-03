# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:03:40 2017

@author: jcf1g17
"""


def positive_places(f, xs):
    """
    takes a string filename which contains the name of a file to be processed.
    The function should open and read that file. The file is expected to
    contain numbers that are separated by commas (the format is known as a
    comma-separated-value file, short csv). The function should compute the
    average value for every line, and return the average values in a list
    """
    lst = []
    for x in xs:
        if f(x) > 0:
            lst.append(x)
        else:
            pass
    return lst


def eval_f_0123(f):
    """
    evaluates the function f=f(x) at positions x=0, x=1, x=2 and x=3. The
    function then returns the list [f(0), f(1), f(2), f(3)].
    """
    lst = []
    i = 0
    while i <= 3:
        lst.append(f(i))
        i = i + 1
    return lst


def eval_f(f, xs):
    """
    takes a function f = f(x) and a list xs of values that should be used as
    arguments for f. The function eval_f will apply the function f
    subsequently to every value x in xs,
    and return a list fs of function values
    """
    lst = []
    for x in xs:
        lst.append(f(x))
    return lst


def sum_f(f, xs):
    """
    returns the sum of the function values of f evaluated at
    values x0, x1, x2, ..., xn where xs=[x0,x1,x2,...,xn]
    """
    lst = []
    for x in xs:
        lst.append(f(x))
    return sum(lst)


def box_volume_UPS(a=13, b=11, c=2):
    """
    returns the volume of a box with edge lengths a, b and c.
    Inputs should be provided in inches,
    and the output should be expressed in inches^3.
    """
    if a != 13:
        boxa = a
    else:
        boxa = 13
    if b != 11:
        boxb = b
    else:
        boxb = 11
    if c != 2:
        boxc = c
    else:
        boxc = 2
    return boxa * boxb * boxc
