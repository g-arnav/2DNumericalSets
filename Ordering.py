# To redefine the ordering function, rewrite less_than

class OrderedPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p2):
        return OrderedPair(self.x+p2.x, self.y+p2.y)

    def sub(self, p2):
        return OrderedPair(self.x-p2.x, self.y-p2.y)

    def mult(self, k):
        return OrderedPair(self.x*k, self.y*k)

    def pos(self):
        return self.x >= 0 and self.y >= 0

    def __repr__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def less_than(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y <= other.y:
            return True
        else:
            return False
