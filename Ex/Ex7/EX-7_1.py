import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def floatrange(start, end, step):
    while(start < end):
        yield start
        start += step

class Point:
    """2D Point class"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)

    def reflect_x(self):
        if self.y > 0:
            new_y = self.y * -1
        else:
            new_y = self.y
        return repr(Point(self.x, new_y))

    def slop_from_origin(self):
        try:
            return self.y / self.x
        except TypeError:
            print("slop_from_origin() missing 1 required positional argument: 'other'")
        except ZeroDivisionError:
            print("Should be Infinite!!")
            return "Infinite"

    def get_line_to(self, other):
        try:
            if other.x == self.x:
                return None
            else:
                slope = (self.y - other.y) / (self.x - other.x)

            b = self.y - (self.x * slope)
            return "y = " + str(int(slope)) + "x + " + str(int(b))
        except TypeError:
            print("can only concatenate str (not float) to str")


    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def midpoint(self, other):  # self <= Point(3, 4), other <= Point(5, 12)
        """ Return the midpoint of points p1 and p2 """
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at Point posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(
            self.corner, self.width, self.height)

    # return f"{self.corner}, {self.width}, {self.height}

    def __repr__(self):
        return "Rectangle({0}, {1}, {2})".format(
            repr(self.corner), self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def flip(self):
        swap = self.width
        self.width = self.height
        self.height = swap

        return self.width, self.height

    def contains(self, Point):
        # if Point.x in range(self.width):
        #     if Point.y in floatrange(0, self.height, 0.00001):
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

        if self.corner.x <= Point.x < self.width and self.corner.y <= Point.y < self.height:
            return True
        else:
            return False


if __name__ == '__main__':
    # Class Point
    # Question 1
    p1 = Point(3, 5)
    p2 = Point(3, 5)
    print(p1 == p2)
    print(p1 != p2)

    # Question 2
    ref_value = Point(3, 5).reflect_x()
    print(ref_value)

    # Question 3
    slop_value = Point(4, 10).slop_from_origin()
    print(slop_value)

    # Question 4
    line_value = Point(4, 11).get_line_to(Point(6, 15))
    print(line_value)

#=================================================================================#
    # Class Rectangle
    # Question 1
    area = Rectangle(Point(0, 0), 12, 10).area()
    print(area)

    # Question 2
    perimeter = Rectangle(Point(0, 0), 12, 10).perimeter()
    print(perimeter)

    # Question 3
    r = Rectangle(Point(100, 50), 10, 5)
    test(r.area() == 50)
    test(r.perimeter() == 30)
    r.flip()
    test(r.width == 5 and r.height == 10)

    # Question 4
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))