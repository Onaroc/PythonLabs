# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:16:05 2017
@author: JFord
"""
import numpy as np
import math


def f(x):
    """
    Input is a number or array and returns the value of f(x) of that number
    or array as the same type.
    """
    if x is float or int:
        return ((math.exp(-(x ** 2)) / (1 + x ** 2)) +
                ((2 * (math.cos(x)) ** 2) / (1 + (x - 4) ** 2)))
    else:
        for a in x:
            a = ((math.exp(-(a ** 2)) / (1 + a ** 2)) +
                 ((2 * (math.cos(a)) ** 2) / (1 + (a - 4) ** 2)))
        return x
