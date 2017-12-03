# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:08:51 2017

@author: jcf1g17 (Jake Ford)
"""

def average(a, b):
    """Given parameters a and b, compute and
       return the arithmetic mean of a and b"""
    return (a + b) * 0.5
def distance(a, b):
    """Given parameters a and b, compute and
       return the arithmetic mean of a and b"""
    if (a - b) >= 0:
       return (a - b)
    else:
       return -(a - b)
def geometric_mean(a, b):
    """returns the geometric mean of two numbers
       i.e. the edge length a square would have to
       have so that its area equals that of a
       rectangle with sides a and b"""
    return (a * b) ** 0.5
def pyramid_volume(A, h):
    """computes and returns the volume of a
       pyramid with base area A and height h"""
    return (A * h) / 3
