import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def mult_of_list(l):
    newList = list(l)
    mul = 1
    for i in newList:
        mul *= i

    return mul

test(mult_of_list([1, 2, 3, 4]) == 24)
test(mult_of_list([1, 20, -3, 4]) == -240)
test(mult_of_list([1, 0, -33, 9999]) == 0)