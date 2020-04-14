class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, z):
        return (Kwadrat(self.x * 4 + z *4))

kw = Kwadrat(4)
print(kw.__add__(8).x)