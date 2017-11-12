# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:48:44 2017
@author: JFord
"""


def count_sub_in_file(filename, s):
    """
    Takes two arguments, 'filename', the name of the file in
    which this function searches and 's', the string this function
    searches for. Returns how many times 's' apears in the file.
    """
    try:
        f = open(filename, 'r')
        text = f.read().split(s)
        f.close
        return len(text) - 1
    except FileNotFoundError:
        return -1


def count_vowels(s):
    """
    Counts how many times the vowels 'a,e,i,o,u,A,E,I,O,U' occur in the
    given string "s" and returns the number as an integer
    """
    lst = []
    for a in s:
        if a in "aAeEiIoOuU":
            lst.append(a)
    return len(lst)


def vector_product3(a, b):
    """
    Takes an input of a and b, two sequences of numbers that contains three
    elements. With inputs a=[ax, ay, az] and b=[bx, by, bz], the function
    returns a list which contains the vector product of 3d-vectors a
    and b, i.e. the return value is the list:
    [ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx].
    """
    lst = []
    lst.append(a[1] * b[2] - a[2] * b[1])
    lst.append(a[2] * b[0] - a[0] * b[2])
    lst.append(a[0] * b[1] - a[1] * b[0])
    return lst


def seq_mult_scalar(a, s):
    """
    takes a list of numbers a and a scalar (i.e. a number) s.
    For the input a=[a0, a1, a2,.., an] the function returns
    [s * a0, s * a1, s * a2, ..., s * an].
    """
    lst = [x * s for x in a]
    return lst


def powers(n, k):
    """
    returns the list [1,n,n^2,n^3,...,n^k] where k is an integer.
    """
    lstk = list(range(k + 1))
    lst = []
    pos = 0
    while pos <= k:
        lst.append(n ** lstk[pos])
        pos = pos + 1
    return lst


def traffic_light(load):
    """
    takes a floating point number load. The function should return the string:
    "green" for values of load below 0.7.
    "amber" for values of load equal to or more than 0.7 but less than 0.9
    "red" for values of load equal to 0.9 or more than 0.9
    """
    if load < 0.7:
        return "green"
    elif load >= 0.7:
        if load >= 0.9:
            return "red"
        else:
            return "amber"
