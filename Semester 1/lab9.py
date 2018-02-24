# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:07:48 2017
@author: jFord
"""
from scipy.integrate import quad


def trapez(f, a, b, n):
    """
    Takes as an input a function f, a lower and upper boundry a and b,
    and a number of subdivisions (n). The function then uses the
    composite trapezoidal rule to compute A and returns this value.
    """
    fa = f(a)
    fb = f(b)
    fab = []
    h = (b - a) / n
    for x in range(0, (n)):
        fab.append(f(a + (h * x)))  # Creates a list of x(0) to x(n-1)
    sumt = (h / 2) * (fa + fb + 2 * sum(fab[1:]))
    return sumt


def fef(x):
    """
    Function for FindError
    """
    return x*x


def finderror(n):
    """
    Uses the trapez() function to find the error of the trapezoidal
    integral approximation. Uses f = x*x, a = -1, b = -2, and takes
    as an input n. The function then subtracts the numerical result
    obtained from the trapez() from the exact integral value (i = 3)
    and returns the difference from i
    """
    i = 3  # i is the exact value of the integration of x^2 between -1 and 2
    val = trapez(fef, -1, 2, n)
    return i - val


def using_quad():
    """
    Useing the function quad from the scipy.intergrate module, returns
    the approximation of the intergral of x^2 between -1 and 2 in the
    form of a tuple (y, abserr) where y is the approximation and abserr
    is the estimate of absolute error
    """
    return quad(fef, -1, 2)


def std_dev(x):
    """
    takes a list x of floating point numbers, and
    computes and returns the corrected sample standard
    deviation of the floating point numbers in the list x
    """
    mu = (1 / len(x)) * sum(x)
    lst = [(a - mu) ** 2 for a in x]
    return((1 / (len(x) - 1)) * sum(lst)) ** 0.5


def encode(code, msg):
    """
    Takes as an inputs a dictionary code and a string msg
    and applies the mapping of the dictionary to each character
    in the string and returns the encoded message
    """
    a = []
    for k in msg:
        if k in code:
            a.append(code.get(k))
        else:
            a.append(k)
    return ''.join(a)


def reverse_dic(d):
    """
    Takes as an input a dictionary d and returns a dictionary r
    If d has a value v and a key k r has a value k and a key v
    """
    k = {v: k for k, v in d.items()}
    return k


def decode(code, encoded_msg):
    """
    takes a dictionary code that contains the mapping dictionary
    with which the string encoded_msg has been encoded.
    The function decode should return the decoded message.
    """
    return encode(reverse_dic(code), encoded_msg)


"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    # lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    # upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    # space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.
    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print("Code is not reversible:")
        print("keys are   %s", sorted(unique_keys))
        print("values are %s", sorted(unique_vals))
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = \
    "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


# if this file is executed on it's own, check codes given
if __name__ == "__main__":
    test_codes()
