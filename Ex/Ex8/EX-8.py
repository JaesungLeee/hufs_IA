class Set:
    def __init__(self, value=[]):  # Constructor
        self.data = []  # Manages a list
        self.concat(value)

    def intersection(self, other):  # other is any sequence
        res = []  # self is the subject
        for x in self.data:
            if x in other:  # Pick common items
                res.append(x)
        return Set(res)  # Return a new Set

    def union(self, other):  # other is any sequence
        res = self.data[:]  # Copy of my list
        for x in other:  # Add items in other
            if not x in res:
                res.append(x)

        print(res)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:  # Removes duplicates
                self.data.append(x)

        return self.data

    def issubset(self, other):
        intersect = []
        for x in self.data:
            if x in other.data:
                intersect.append(x)

        if self.data == intersect:
            if len(self.data) == len(other.data):
                print("self <= other")
            elif len(self.data) < len(other.data):
                print("self < other")
        else:
            print("None")


    def issuperset(self, other):
        intersect = []
        for x in other.data:
            if x in self.data:
                intersect.append(x)

        if other.data == intersect:
            if len(self.data) == len(intersect):
                print("self >= other")
            elif len(self.data) > len(intersect):
                print("self > other")
        else:
            print("None")

    def intersection_update(self, other):
        self.data = [x for x in self.data if x in other.data]
        print("self &= other")


    def difference_update(self, other):
        self.data = [x for x in self.data if x not in other.data]
        print("self -= other")

    def symmetric_difference_update(self, other):
        union = self.data[:]
        for i in other.data:
            if i not in union:
                union.append(i)

        intersect = [x for x in self.data if x in other.data]

        result = []
        for i in union:
            if i not in intersect:
                result.append(i)

        self.data = result
        print("self ^= other")

    def add(self, elem):
        if elem in self.data:
            return self.data
        else:
            self.data.append(elem)
            return self.data

    def remove(self, elem):
        if elem in self.data:
            self.data.remove(elem)
            return self.data
        else:
            raise KeyError ("No element in set")

    def __len__(self):
        return len(self.data)  # len(self)

    def __getitem__(self, key):
        return self.data[key]  # self[i], self[i:j]

    def __and__(self, other):
        return self.intersection(other)  # self & other

    def __or__(self, other):
        return self.union(other)  # self | other

    def __repr__(self):
        return 'Set({})'.format(repr(self.data))

    def __iter__(self):
        return iter(self.data)  # for x in self:

    def __iand__(self, other):
        return self.intersection_update(other)

    def __isub__(self, other):
        return self.difference_update(other)

    def __ixor__(self, other):
        return self.symmetric_difference_update(other)



if __name__ == '__main__':
    # x = Set([1, 3, 5, 7, 1, 3])
    # y = Set([2, 1, 4, 5, 6])
    # print(x, y, len(x))
    # print(x.intersection(y), y.union(x))
    # print(x & y, x | y)
    # print(x[2], y[:2])
    # for element in x:
    #     print(element, end=' ')
    # print()
    # print(3 not in y)  # membership test
    # print(list(x))  # convert to list because x is iterable

    print("="*21, "Check issubset", "="*21)
    x = Set([1, 3, 5, 3])
    y = Set([1, 3, 5, 7, 9])
    print("x :", x)
    print("y :", y)
    x.issubset(y)
    print()

    print("="*20, "Check issuperset", "="*20)
    x = Set([1, 2, 5, 6, 7])
    y = Set([5, 6, 5])
    print("x :", x)
    print("y :", y)
    x.issuperset(y)
    print()

    print("="*15, "Check intersection_update", "="*16)
    x = Set([1, 2, 5, 6, 7, 2])
    y = Set([5, 6, 4])
    print("x :", x)
    print("y :", y)
    x.intersection_update(y)
    print("Now x is.. : {}".format(x))
    print()

    print("=" * 16, "Check difference_update", "=" * 17)
    x = Set([1, 2, 1, 4, 2, 0])
    y = Set([5, 6, 3, 6])
    print("x :", x)
    print("y :", y)
    x.difference_update(y)
    print("Now x is.. : {}".format(x))
    print()

    print("=" * 11, "Check symmetric_difference_update", "=" * 12)
    x = Set([1, 2, 9, 4, 1, 2])
    y = Set([5, 6, 3, 6])
    print("x :", x)
    print("y :", y)
    # x |= y
    # print("ssssssssx:", x)
    x.symmetric_difference_update(y)
    print("Now x is.. : {}".format(x))
    print()

    print("=" * 23, "Check add", "=" * 24)
    x = Set([1, 2, 9, 4, 1, 2])
    print("x :", x)
    x.add(8)
    print("Now x is.. : {}".format(x))
    print()

    print("=" * 22, "Check remove", "=" * 23)
    print("x :", x)
    x.remove(100)
    print("Now x is.. : {}".format(x))