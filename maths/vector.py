from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return Vector(other.x - self.x, other.y - self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def round(self):
        return Vector(int(self.x), int(self.y))

    def normalize(self):
        l = self.length()
        return Vector(self.x/l, self.y/l)
