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


def non_recursive_factorial(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact

test(non_recursive_factorial(5) == math.factorial(5))
test(non_recursive_factorial(8) == math.factorial(8))
test(non_recursive_factorial(2) == math.factorial(2))
test(non_recursive_factorial(10) == math.factorial(10))