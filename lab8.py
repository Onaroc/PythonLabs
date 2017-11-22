# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:11:06 2017
@author: JFord
"""
import math
import matplotlib.pyplot as plt
from scipy import optimize


def f(x):
    return x * x


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
    return math.log(x + 2.2)


def positive_places(f, xs):
    """
    Takes as an argument a function f and a list
    of numbers xs and returns a list of those and
    only those elemnts x of xs for which f(x) is
    strictly greater than zero
    """
    lst = [v for v in xs if (f(v) > 0)]
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
    ys = [f(x) for x in xs]
    return (xs, ys)


def myplot():
    """
    Computes and plots f1(x) and f2(x) (using create_plot_data)
    on a graph between -2 and 2 for 1001 points, then
    returns none
    """
    xdataf1 = (create_plot_data(f1, -2, 2, 1001))[0]
    xdataf2 = (create_plot_data(f2, -2, 2, 1001))[0]
    ydataf1 = (create_plot_data(f1, -2, 2, 1001))[1]
    ydataf2 = (create_plot_data(f2, -2, 2, 1001))[1]
    plt.plot(xdataf1, ydataf1, label='f1')
    plt.plot(xdataf2, ydataf2, label='f2')
    plt.xlabel('f(x)')
    plt.legend(loc='upper left')
    plt.show
    plt.savefig('plot.png')
    plt.savefig('plot.pdf')
    return None


def g(x):
    return f1(x) - f2(x)


def find_cross():
    """
    finds and returns an approximation for the root of
    f1(x) = f2(x) using brents method (from the scipy library)
    """
    rootx = optimize.brentq(g, a=0, b=2)
    return rootx


def reverse_dic(d):
    """
    Takes as an input a dictionary d and returns a dictionary r
    If d has a value v and a key k r has a value k and a key v
    """
    k = {v: k for k, v in d.items()}
    return k
