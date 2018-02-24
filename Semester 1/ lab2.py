# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:33:26 2017
@author: JFord
"""


def box_volume(a, b, c):
    """
    calculates and returns the volume of
    a cuboid with edge lengths a, b, c.
    """
    return(a * b * c)


def fall_time(h):
    """
    returns the time (in seconds) needed
    for an object falling from a tower
    of height h (in meters) to hit the
    ground (ignoring air friction).
    """
    return ((2 * h) / 9.81) ** (1/2)


def interval_point(a, b, x):
    """
    given a and b as the start and end point of an
    interval, and x as a fraction between 0 and 1 that
    determines how far to go towards b, starting at a, returns
    the interval point at this fraction of the way along
    """
    return (a + (b - a) * x)


def impact_velocity(h):
    """
    returns the velocity (in metres per second)
    with which an object falling from a height
    of h meters will hit the ground.
    """
    return (((2 * h) / 9.81) ** (1/2)) * 9.81


def signum(x):
    """
    given a number x returns:
    1 if x > 0
    0 if x = 0
    -1 if x < 0
    """
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def seconds2days(n):
    """
    returns the number of days (as a float or
    int value) that are present in n seconds
    """
    return n / 86400


def box_surface(a, b, c):
    """
    returns the surface area of a box with
    sides length a, b, and c
    """
    return 2 * ((a * b) + (b * c) + (c * a))


def triangle_area(a, b, c):
    """
    returns the area of a triangle that
    has edge lengths a, b, and c
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** (1/2)
