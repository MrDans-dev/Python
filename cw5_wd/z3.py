class gt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __gt__(self):
        return self.x > self.y
a = gt(20, 50)
print(a.__gt__())

class ge:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __ge__(self):
        return self.x >= self.y
a = ge(20, 50)
print(a.__ge__())

class lt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self):
        return self.x < self.y
a = lt(20, 50)
print(a.__lt__())

class le:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __le__(self):
        return self.x <= self.y
a = le(20, 50)
print(a.__le__())