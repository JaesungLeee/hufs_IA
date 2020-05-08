import sys
import math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def my_gcd(a, b):
    if a < 0 or b < 0:
        a = -a
        b = -b

    max_n = max(a, b)
    min_n = min(a, b)

    gcd = max_n % min_n
    while gcd > 0:
        max_n = min_n
        min_n = gcd
        gcd = max_n % min_n
    result = min_n

    return  result

test(my_gcd(12, 16) == math.gcd(12,16))
test(my_gcd(16, 12) == math.gcd(16, 12))
test(my_gcd(9, 6) == math.gcd(9, 6))
test(my_gcd(-12, -38) == math.gcd(-12, -38))