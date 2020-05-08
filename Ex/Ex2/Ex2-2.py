import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def sum_of_digit_square(n):
    sum = 0
    if n < 0:
        n = n * -1

    str_n = str(n)
    str_list = str(str_n)

    for i in str_list:
        digit = int(i)
        sum += digit**2
    return sum

test(sum_of_digit_square(789) == 7 ** 2 + 8 ** 2 + 9 ** 2)
test(sum_of_digit_square(-123) == 1 ** 2 + 2 ** 2 + 3 ** 2)