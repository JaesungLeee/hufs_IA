# Q3. Q2와 동일하지만 generator로 구현한 xrange() 함수를 작성하라.
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def xrange(start, stop = None, step = 1):
    if start == 0 and stop == None:
        return None
    elif start != 0 and stop == None:
        stop = start
        start = 0
    for i in range(start, stop, step):
        yield i


print(xrange(4))
test(list(xrange(4)) == [0, 1, 2, 3])
test(list(xrange(4)) == list(range(4)))
test(sum(i for i in xrange(1, 11)) == 55)
test(list(xrange(-1, 7, 2)) == list(range(-1, 7, 2)))
test(list(xrange(10, 1, -2)) == list(range(10, 1, -2)))