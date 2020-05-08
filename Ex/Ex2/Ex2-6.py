import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def unit_place_value(n):
    sum = 0
    if n < 10:
        return n
    str_n = str(n)
    n_list = list(str_n)
    for i in n_list:
        sum += int(i)
        result = sum
    return unit_place_value(result)


test(unit_place_value(75) == 3)
test(unit_place_value(3942) == 9)
test(unit_place_value(32) == 5)
test(unit_place_value(9) == 9)