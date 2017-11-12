# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:13:04 2017
@author: JFord
"""
import urllib.request


def line_averages(filename):
    """
    Takes a string "filename" and open and reads the file with the
    cooresponding name. The function then splits each line into a list
    and calculates the mean of these lists and returns a list that
    contains the mean of each line in order.
    """
    f = open(filename, 'r')
    lines = f.read().splitlines()
    f.close
    mean_list = []
    for l in lines:
        li = []
        li = l.split(',')
        lst = [float(i) for i in li]
        length = len(lst)
        sumfile = sum(lst)
        mean_list.append(sumfile / length)
    return mean_list


def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


def noaa_temperature(s):
    """
    Takes an input string "s" and extracts the temperature in degree
    Celsius from the string, returning this temperature as an integer number
    """
    lst = s.splitlines()
    temp = "Temperature"
    testdigit = []
    digit = (" (")
    tempdigit = ("(")
    neg = ("-")
    for a in lst:
        if temp in a:
            testdigit = a[-6:-3]
            if digit in testdigit:
                return int(testdigit[2])
            elif neg in testdigit:
                if tempdigit in testdigit:
                    return int(testdigit[1:])
                else:
                    return int(testdigit)
            else:
                return int(testdigit[1:])


def seq_sqrt(xs):
    """
    takes a list of non-negative numbers xs with elements
    [x0, x1, x2, ..., xn], and returns the list:
    [sqrt(x0), sqrt(x1), sqrt(x2), ..., sqrt(xn)]
    """
    sqrtlst = [x ** (1 / 2) for x in xs]
    return sqrtlst


def mean(xs):
    """
    takes a sequence xs of numbers, and returns
    the (arithmetic) mean (i.e. the average value)
    """
    return sum(xs) / len(xs)


def wc(filename):
    """
    'WC' or Word Count returns the number of words in file "filename"
    """
    f = open(filename, 'r')
    words = f.read().split()
    f.close
    return len(words)
