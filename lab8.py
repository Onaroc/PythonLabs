# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:11:06 2017
@author: JFord
"""
import math


def f1(x):
    """
    Accepts a number x as an input and returns
    cos(2*pi*x)*exp(-x^2)
    """
    return math.cos(2 * math.pi * x) * math.exp(-x ** 2)


def f2(x):
    """
    Accepts a number x as an input and returns
    log (x + 2.1)
    """
    return math.log(x + 2.1)


def positive_places(f, xs):
    """
    Takes as an argument a function f and a list
    of numbers xs and returns a list of those and
    only those elemnts x of xs for which f(x) is
    strictly greater than zero
    """
    lst = [f(x) for x in xs if (f(x) > 0)]
    return lst


def create_plot_data(f, xmin, xmax, n):
    """
    Returns a tuple (xs, ys)
    where xs and ys are two sequences
    each containing n numbers
    """
    xs = []
    ival = range(n)
    for i in ival:
        xi = xmin + i * ((xmax - xmin) / (n - 1))
        xs.append(xi)
    xy = [f(x) for x in xs]
    return (xs, xy)


