# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:09:21 2017
@author: JFord
"""


def count_chars(s):
    """
    Takes a string 's' and returns a dictionary. The dictionary's keys
    are the set of characters the occur in the string. The value for each
    key is the amount of times each character appears.
    """
    dct = {x: s.count(x) for x in s}
    return dct


def derivative(f, x, eps=1e-6):
    """
    Computes and returns a numerical approximation of the first
    derivative of the function f(x) using central differences.
    """
    return (f(x + (eps / 2)) - f(x - (eps / 2))) / eps


def newton(f, x, feps, maxit):
    """
    Takes as an input the function f, an intial guess x for the root of
    the equation f(x), an allowed tolerance feps and a maximum number of
    iterations maxit, then returns the result of a newton-rhapson iteration
    with the aforementioned parameters.
    """
    errmax = maxit
    while maxit > 0:
        if abs(f(x)) > feps:
            x = x - f(x) / derivative(f, x)
            maxit = maxit - 1
        else:
            return x
    raise RuntimeError("Failed after {} iterations".format(errmax))


def is_palindrome(s):
    """
    Takes in a string s and returns true if s is a palindrome
    or false if s is not a palindrome.
    """
    length = len(s)
    pos = len(s)
    ispal = 0
    while pos > 0:  # Note this does twice the amount of calcs needed
        if s[pos - 1] != s[length - pos]:
            ispal = ispal + 1
        pos = pos - 1
    if ispal > 0:
        return False
    else:
        return True
