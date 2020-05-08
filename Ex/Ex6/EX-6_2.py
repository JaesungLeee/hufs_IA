# Q2.
# list를 return하되, 다만, 다음과 같은 형식으로 argument를 받을 수 있는 함수 lrange(start, stop, step)를 작성하라.
#
# lrange(start, stop): 3번째 argument가 생략되면 step=1
# lrange(stop): 1번째 3번째 argument가 생략되면, start=0, step=1
# Hint: parameter stop이 생략되면 None이 되게 해보자.

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def lrange(start, stop = None, step = 1):
    result_list = []
    if start == 0 and stop == None:
        return None
    elif start != 0 and stop == None:
        stop = start
        start = 0
    for i in range(start, stop, step):
        result_list.append(i)
    return result_list

print(lrange(4))
test(lrange(4) == [0, 1, 2, 3])
test(sum(i for i in lrange(1, 11)) == 55)
test(lrange(-1, 7, 2) == list(range(-1, 7, 2)))
test(lrange(10, 1, -2) == list(range(10, 1, -2)))