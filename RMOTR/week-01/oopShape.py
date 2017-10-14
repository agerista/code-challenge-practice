class Shape(object):
    def area(self):
        raise NotImplementedError()


class Circle(Shape):

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, height, width):
        super(Rectangle, self).__init__()
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Square(Rectangle):

    def __init__(self, side):
        super(Square, self).__init__(side, side)
        self.side = side


#############################################################
c = Circle(radius=10)
c.area()  # 314.0 (3.14 * 10 * 10)

s = Square(side=4)
s.area()  # 16 (4 * 4)

r = Rectangle(height=4, width=3)
r.area()  # 12 (4 * 3)


def test_square():
    s = Square(side=4)
    assert s.area() == 16


def test_circle():
    c = Circle(radius=10)
    assert c.area() == 314.0


def test_rectangle():
    r = Rectangle(height=4, width=3)
    assert r.area() == 12

print test_square()
print test_circle()
print test_rectangle()
