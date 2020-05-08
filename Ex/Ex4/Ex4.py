import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# 종류 별로 count하자: dict 이용
# 먼저 과일들의 list를 만들자: ['an apple', 'a banana', 'two oranges', ... ]
# join method로 콤파를 삽입한다.

def sentence(basket):
    mo = ['a', 'e', 'i', 'o', 'u']

    b_list = list(set(basket))
    b_list.sort()
    # print(b_list)

    fruit_count = {}
    for i in basket:
        count = basket.count(i)
        fruit_count[i] = count
    # print(fruit_count)

    fruit_list = []
    for i in b_list:
        j = i
        if fruit_count[i] == 1 :     # 과일 한개
            if i[0] in mo:
                fruit_list.append('an ' + i)
            else :
                fruit_list.append('a ' + i)
            # print(fruit_list)

        elif fruit_count[i] > 1:    # 과일 두개 이상
            if i.endswith('x' or 's' or 'sh' or 'ch') :
                i = i + 'es'
                # fruit_list.append(i)
            elif (i[len(i) - 2] not in mo) and i.endswith('y') :
                i = i[0:len(i) - 1] + 'ies'
                # fruit_list.append(i)
            elif i.endswith('f') :
                i = i[0:len(i) - 1] + 'es'
                # fruit_list.append(i)
            elif i.endswith('fe') :
                i = i[0:len(i) - 2] + 'ves'
                # fruit_list.append(i)
            else:
                i = i + 's'
                # fruit_list.append(i)

            if fruit_count[j] == 2 :
                fruit_list.append('two ' + i)
            elif fruit_count[j] >= 3 :
                fruit_list.append('many ' + i)
    # print(fruit_list)

    if len(fruit_list) > 1:
        fruit_list[len(fruit_list) - 1] = 'and ' + fruit_list[len(fruit_list) - 1]
        result = ', '.join(fruit_list)
        return "There are " + result + " in the basket."
    else :
        result = ', '.join(fruit_list)
        return "There is" + result + " in the basket."


fruits = ['orange', 'pear', 'pear', 'apple', 'orange', 'banana']
test(sentence(fruits) == 'There are an apple, a banana, two oranges, and two pears in the basket.')
many_oranges = ['apple', 'orange', 'orange', 'orange', 'pear', 'orange']
test(sentence(many_oranges) == 'There are an apple, many oranges, and a pear in the basket.')